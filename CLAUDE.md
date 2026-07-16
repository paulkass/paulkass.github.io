# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository

Personal website for Paul Kassianik, published via GitHub Pages from the `paulkass/paulkass.github.io` repository. The site is served at the root of `paulkass.github.io` and built automatically by GitHub Pages on push to `main` — there is no local build step in this repo.

## Stack

Jekyll site using the `jekyll-theme-minimal` remote theme (configured in `_config.yml`). Because the site uses a stock GitHub Pages theme and currently has no overrides, layouts/includes/assets are inherited from the theme — they don't exist in this repo unless explicitly added to override the theme.

## Local preview (when needed)

There is no committed Gemfile. To preview locally, create one pinning `github-pages` and run `bundle exec jekyll serve` — GitHub Pages itself does the build on push, so local tooling is only for previewing changes before committing.
