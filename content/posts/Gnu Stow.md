---
title: Stow - An amazing tool for dotfiles
date: 2025-06-27
draft: false
tags:
  - Linux
---

## **Introduction**

So today i was thinking about backing up my dotfiles. I am going to be using linux at my job so i needed an easy way of getting my system up and running. That is when I discovered an amazing tool, GNU stow. 

## **What is GNU stow?**

GNU stow is a symlink farmmanager [gnu.org](https://www.gnu.org/software/stow/). In simpler terms this means it is an easy way of setting up symlinks. This makes it possible to have one folder with all your dotfiles, and with one command you can link them all to the right places on your system.

## **Setting up stow**

The setup process was simple enough, I made a folder with the name .config and added all files that go into .config on my system into it. Which looks something like this:
```
dotfiles/.config/

├── alacritty/
│   ├── alacritty.toml
│   └── dracula.toml
├── fastfetch/
│   └── config.jsonc
├── fish/
│   ├── completions/
│   ├── conf.d/
│   ├── config.fish
│   ├── fish_variables
│   └── functions/
│       └── fish_prompt.fish
├── gtk-3.0/
│   ├── bookmarks
│   └── settings.ini
├── gtk-4.0/
│   └── settings.ini
├── mako/
│   └── config
├── rofi/
│   ├── config.rasi
│   ├── rofi-exit.sh
│   ├── rofi-wifi-menu.sh
│   ├── scriptLauncher.sh
│   └── scripts/
│       ├── calculator.sh
│       ├── currency.sh
│       ├── hardware.sh
│       └── measure.sh
├── sway/
│   ├── autostart
│   ├── binds
│   ├── config
│   ├── scripts/
│   │   ├── display-autoset.sh
│   │   ├── display-menu.sh
│   │   └── songnotify.sh
│   ├── theme
│   └── windowRules
├── swaylock/
│   ├── config
│   └── dracula-wallpaper.svg
└── waybar/
    ├── config
    ├── scripts/
    │   ├── .env
    │   ├── .env-example
    │   ├── batteryNotify.sh
    │   ├── brightness.sh
    │   ├── notify-toggle.sh
    │   ├── open_weather.sh
    │   ├── swayidle_status.sh
    │   ├── swayidle_toggle.sh
    │   └── weather.py
    └── style.css
```

So my dotfiles are now all in a .config folder just not in my home directory. I can now run `stow .` in the dotfiles directory and all the files get placed in the correct places.

## **Setting up a repo**

I could then set up a repo for this. I also added a couple of other files. One where i took all the packages I've installed so i could install everything in one line. I did this using the command `pacman -Qqe > pkglist.txt` then i filtered out all the aur packages and put them into another file. These could then be installed using the command `sudo pacman -S --needed - < pkglist.txt` and the same for aur just using [paru](https://aur.archlinux.org/packages/paru-bin) or [yay](https://aur.archlinux.org/packages/yay-bin).

## **Final thoughts**

Stow is an awesome tool that makes organizing, backing up and sharing dotfiles so much easier. In the past I have spent so much time making scripts to do this exact thing, when stow is so much easier to keep track of. I think more people should know about this piece of software. I really think this could be super usefull for people who share their dotfiles on [r/unixporn](https://www.reddit.com/r/unixporn/).