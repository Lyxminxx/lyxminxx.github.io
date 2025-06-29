import os
import shutil
import re
import markdown
import yaml
from pathlib import Path
from datetime import datetime, date as date_type
from markdown import Markdown

# Custom Markdown parser that disables auto-linking
class NoAutolinkMarkdown(Markdown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inlinePatterns.deregister('autolink')  # removes <http://example.com> style autolinks

VAULT_DIR = "/home/madelen/Documents/blog/posts"
OUTPUT_DIR = "posts"
ATTACHMENTS_SRC = "/home/madelen/Documents/blog/attachments"
ATTACHMENTS_DST = "attachments"
TEMPLATE_FILE = "template/template.html"
BLOG_INDEX = "blog.html"

def parse_markdown_with_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith('---'):
        parts = content.split('---', 2)
        frontmatter = yaml.safe_load(parts[1])
        markdown_content = parts[2]
    else:
        frontmatter = {}
        markdown_content = content

    return frontmatter, markdown_content

def fix_obsidian_image_links(md_content):
    pattern = r'!\[\[([^\]]+)\]\]'
    def replacer(match):
        filename = match.group(1).strip()
        return f'![](../attachments/{filename})'
    return re.sub(pattern, replacer, md_content)

def load_template():
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def convert_posts(template):
    posts = []

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(VAULT_DIR):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(VAULT_DIR, filename)
        frontmatter, md_content = parse_markdown_with_frontmatter(filepath)

        if frontmatter.get("draft", False):
            continue

        date_str = frontmatter.get("date", "1970-01-01")
        if isinstance(date_str, date_type):
            date = date_str
        else:
            date = datetime.strptime(date_str, "%Y-%m-%d")

        title = frontmatter.get("title", "Untitled") or "Untitled"
        fixed_md = fix_obsidian_image_links(md_content or "")

        html_content = markdown.markdown(
            fixed_md,
            extensions=["fenced_code", "codehilite"],
            extension_configs={
                "markdown.extensions.codehilite": {
                    "guess_lang": False,
                    "noclasses": True 
                }
            },
            output_format="html5"
        )

        slug = Path(filename).stem
        full_html = template.replace("{{title}}", title).replace("{{content}}", html_content)

        out_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        posts.append({
            "title": title,
            "date": date,
            "filename": f"{slug}.html"
        })

    return sorted(posts, key=lambda x: x["date"], reverse=True)

def write_blog_index(posts):
    links = "\n".join([
        f'<li><a href="posts/{p["filename"]}">{p["title"]} ({p["date"].strftime("%Y-%m-%d")})</a></li>'
        for p in posts
    ])

    index_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Blog</title>
  <link rel="stylesheet" href="blog.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="mobile.css">
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
</head>
<body>
  <nav>
    <div class="nav-left">
        <label>&lt;/lyx&gt;</label>
        <a href="/index.html">Home</a>
        <a href="/blog.html">Blog</a>
        <a href="/projects.html">Projects</a>
    </div>
    <div class="nav-right">
        <a href="https://github.com/Lyxminxx" class="socials">Github</a>
        <a href="https://social.linux.pizza/@Madelen" class="socials">Mastodon</a>
    </div>
    </nav>
  <main>
    <h1>Blog Posts</h1>
    <ul>
      {links}
    </ul>
  </main>
</body>
</html>
"""
    with open(BLOG_INDEX, "w", encoding="utf-8") as f:
        f.write(index_html)

def copy_attachments():
    if os.path.exists(ATTACHMENTS_DST):
        shutil.rmtree(ATTACHMENTS_DST)
    shutil.copytree(ATTACHMENTS_SRC, ATTACHMENTS_DST)

if __name__ == "__main__":
    template = load_template()
    posts = convert_posts(template)
    write_blog_index(posts)
    copy_attachments()
    print("Blog updated!")
