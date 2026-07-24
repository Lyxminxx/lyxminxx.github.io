---
title: "COSMIC: The only DE I can use"
date: 2026-03-29
draft: false
tags:
  - Linux
---
## Introduction
I have been on a long Linux journey, where I have tried a bunch of distros and window managers. I started on Mint with cinnamon and I fell in love with Linux. After a while I found tiling window managers, and thought I want to be an awesome Linux user too! I installed i3wm and was confused by the lack of functionality. I looked up a guide and slowly managed to get a usable system. From that moment I could no longer use floating window managers. I hated using windows for school because it lacked tiling. Any tiling window manager I tried on windows sucked so much, and felt like a hacky script not a good environment. I slowly played around more with tiling window managers, sticked mostly to i3 since it was easy and I already had a config. Then wayland came and I moved to sway. 

## Sway
I like sway, it's simple and it was easy to transition from i3. I did a lot of rewrites of my config, making it as easy to use as possible. When I moved to sway I was only using laptops, so a big thing for me was seamless switching to docked mode. I made a hacky script that did the switching for me, because I had not seen a good solution for monitors on sway yet. After a lot of configuration and picking software my sway config worked. It did what I wanted from my system, but everything was a little jank? I felt like my system had weird quirks and it was missing the polish I want from my system. Simple things like monitors, although I am pretty sure there are good solutions for this now. I wanted a system that just works. Where I don't have to think.

## Gnome
Yes, you read that correctly I switched to Gnome. This was when I started working, and I wanted my system to just work. I was on Ubuntu, since everyone else who used Linux at work used it. I used a lot of tweaks including PaperWM. PaperWM works, but Gnome was never meant to be a twm. Just like windows, it felt off. Sure it works, but it always was a little wrong.

## KDE
Another mainstream desktop environment? Yes, I switched to Debian after some computer issues I thought was snaps fault (it was dead ram...). I installed it with KDE since I still wanted an easy experience. I tried using KDE like a floating wm, but this was just not working out. I tried a script for KDE to tile things, and tried sticking with it. Everything still felt off however. After trying to make KDE into a twm I decided enough is enough, I need something built for tiling. This is when I remembered a certain desktop environment written in rust.

## COSMIC: A return to tiling
I remembered COSMIC, a DE that was talked about a lot in it's early development. A system that I always found awesome, it took what pop shell did and made it so much better. I had not used it much yet since it was in early development, but after it's first stable release (I will get back to this) I thought it was time. Now since it's early in development there were some issues with installing it. On my personal laptop I was running arch at the time so it was an easy install as COSMIC is in the official repo. As for my work machine, it was still running Debian. Debian currently does not have any release of COSMIC. I looked online and found a [php script that installs COSMIC](https://codeberg.org/ashimokawa/COSMIC-debian-installer) using fedora packages. I ran this script and COSMIC was installed. This is not a good solution in my opinion, but it works.

## Using COSMIC
Now is when I get back to COSMIC having a stable release... System76 claim COSMIC is stable, but I would argue it still should've been in alpha. I have so many small things that are weird about COSMIC. Nothing is breaking in a major way, which is why I am guessing they call COSMIC stable. Weird window behavior happens, games launch weird and sometimes i need to alt+tab a bit for the window to focus correctly. It's small things, but too big of issues to where I would call it ready for stable release. Now this has not been a major issue, as I fix most things or just ignore the small things. What COSMIC provides me, makes those small things not matter. 

The thing about COSMIC is, I can make it look and function like how I use my window manager without having to do a ton of work. I can change one keybind (mod+d for app launcher), turn of the dock and change the applets in the panel and have a great system. I make it look like a window manager, but it has all the easy parts of a desktop environment. Things like monitors just working, and docking not requiring anything extra. I can import a theme [(I use gruvbox)](https://COSMIC-themes.org/160/) and all my main applications just use that theme. It just works. 

Another thing I really love about COSMIC is that all changed to the system are saved in a folder in .config. This means you can make your COSMIC setup reproducible across all machines using stow and git. I don't have to spend time tweaking things, because everything is just a few clicks in a menu. To me this is a plus, for some it might be annoying.

I now use fedora COSMIC spin on my personal laptop, and nix os with COSMIC at work. I tried using a flake that made it possible to configure COSMIC in home manager, but it was not optimal so I recently removed it and set it up manually. I am planning on moving my work laptop over to fedora as well, but I am waiting on a time where I am less busy at work. I don't really want down time because of set up of the projects I work on. 

## Final thoughts
COSMIC isn't perfect. It still has quirks. But after years of chasing the perfect Linux setup, it's the first system where I stop thinking about the system and just use it. If you've been on a similar journey bouncing between window managers and desktop environments, tweaking endlessly COSMIC might be worth your time.



