#!/bin/bash
set -euo pipefail

# Change to the script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# --- CONFIGURATION ---
sourcePath="/home/madelen/Documents/obsidianVault/posts/"
destinationPath="/home/madelen/codecave/lyxminxx.github.io/content/posts"
myrepo="lyxminxx.github.io"
deployBranch="website"
# ---------------------

# Check for required commands
for cmd in git rsync python3 hugo; do
    if ! command -v $cmd &> /dev/null; then
        echo "$cmd is not installed or not in PATH."
        exit 1
    fi
done

# Step 1: Initialize Git if necessary
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
    git remote add origin $myrepo
else
    echo "Git repository already initialized."
    if ! git remote | grep -q 'origin'; then
        git remote add origin $myrepo
    fi
fi

# Step 2: Sync posts from Obsidian
echo "Syncing posts from Obsidian..."
[ ! -d "$sourcePath" ] && { echo "Source path missing"; exit 1; }
[ ! -d "$destinationPath" ] && { echo "Destination path missing"; exit 1; }

rsync -av --delete "$sourcePath" "$destinationPath"

# Step 3: Process image links
echo "Processing image links..."
if [ -f "images.py" ]; then
    python3 images.py
else
    echo "Warning: images.py not found, skipping processing."
fi

# Step 4: Build the Hugo site
echo "Building the Hugo site..."
hugo --gc --minify

# Step 5 & 6: Commit Source Files to Main
echo "Staging and committing source changes..."
git add .
# Only commit if there are changes
if ! git diff --cached --quiet; then
    git commit -m "Source update: $(date +'%Y-%m-%d %H:%M:%S')"
    echo "Pushing source to main..."
    git push origin main
else
    echo "No source changes to commit."
fi

# Step 7: Deploy 'public' folder to GitHub Pages branch
echo "Deploying 'public' folder to $deployBranch branch..."

# Delete local temp branch if it exists
git branch -D temp-deploy-branch 2>/dev/null || true

# Use subtree split to isolate the 'public' folder into its own commit history
git subtree split --prefix public -b temp-deploy-branch

# Force push the temp branch to your remote 'website' branch
if git push origin temp-deploy-branch:$deployBranch --force; then
    echo "Successfully deployed to $deployBranch!"
else
    echo "Deployment failed."
    exit 1
fi

# Cleanup local temp branch
git branch -D temp-deploy-branch

echo "All done! Site is live on the $deployBranch branch."
