---
title: Windows File Documentation
layout: base
---

## Find information about a Windows binary
This site is structured exactly like a C:\ drive on a normal Windows Desktop installation. To find documentation on the file you are looking for, just add its path to the end of this site's URL. For example, the documentation for calc.exe can be found at:

[`https://winbin.wtf/Windows/System32/calc.exe`](./Windows/System32/calc.exe)

If you can't find the page for the file you are looking for, then its documentation doesn't exist yet.

## Scope

The scope of this documentation is only files that come with a base install of any Windows Desktop version. This does not include opt-in binaries installed by the control panel item "Turn Windows features on or off." If/when all default Windows binaries are documented or this project receives more support, the scope of the documentation may expand.

## For power users

For programmatic access to this data, it's best to clone the [GitHub repo](https://github.com/lawndoc/winbin.wtf) and extract the data from the YAML frontmatter of each document. If this project gets popular enough, maybe we will add a REST and/or GraphQL API for easier access.
