# README

**NOT MAINTAINED**

Better use `md_to_conf` which does this and better.

This project transforms documentation in markdown format into confluence pages.

## Get started

You will need to install `pandoc` tool.

Set up your settings in `$HOME/.confluencer.conf` or `confluencer.conf`.

Then execute:

```
html_to_confluence "Title of the new page" file.html # to publish an HTML file
```

```
markdown_to_confluence "Title of the new page" file.md # to publish a markdown file
```

