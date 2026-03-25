---
title: Hugo again?
date: 2026-03-25
draft: false
tags: []
---
## Introduction
In a previous blog post I talked about building my website. I used an over complicated method of markdown to html conversion in python. The script I made was fully made my Chat gpt and was honestly just a mess. The website was pretty cool, but when I wanted to make a small change to styling I had to change it in multiple places. If my header changed I had to change it on every page. After a bit I have now moved over to Hugo, but why?

## Why Hugo?
I had been planning on doing a rewrite of my website for a while, I wanted something very minimal that just works. After putting it off for months I saw a video from [DT](https://youtu.be/onw826NsgWQ?si=ofXDkhXsrpugq6bO) about Hugo. In a [previous blog](https://maddiemightcry.space/posts/building-my-website/) post I talked about why I moved away from Hugo. I gave reasons like "I don't care for frameworks with strict rules" and how I had issues setting it up on a new computer. I still like simplicity, but that is also kind of why I moved over to Hugo. It's weird, but the script "I made" and the flow was just too complicated. When I saw DT's video I remembered exactly how elegant Hugo actually is. So I decided to give it a shot.

## The setup
Setup was pretty easy, and only took an hour or so. I used a simple theme called ["No style please!"](https://github.com/hanwenguo/hugo-theme-nostyleplease), so I did not have to write any CSS. I modified the homepage a little, and set up the [mega script from network chuck](https://blog.networkchuck.com/posts/my-insane-blog-pipeline/#linuxmac-bash) with some modifications for it to be used only for GitHub pages not Hostinger. After that, I had to add my CNAME file to the public folder, and then I ran my script. I then ran into an issue, I could not make a subtree. The command git subtree was nowhere to be found. First I thought It might've been because subtree's was deprecated. It didn't really make sense to me, but why would it not be there? After some digging I found out it was a separate package, at least on fedora which I am running right now. After installing subtrees, everything works great. I now have easy to use blog posts and in the future I will add more pages of content. 

## RSS
The theme I am using came with rss already set up. That means when I make a blog post it will update the rss feed, so please add it to your reader if you wish. The url is https://maddiemightcry.space/index.xml. 

## Final thoughts
Hugo was pretty easy to set up. The mega script from NetworkChuck does some heavy lifting, but the simpicity of everything is great. I don't know if I will stick with Hugo forever, but for now it does exactly what I need it to. 