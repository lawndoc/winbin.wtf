# WinBin.wtf

This repo contains the source code for [WinBin.wtf](https://winbin.wtf), a Windows binary documentation site. The site is intended to make up for Microsoft's lack of documentation on Windows binaries.

The directory structure is laid out exactly like the C:\ drive would be on a normal Windows installation, so you just need to append the path of the file you are looking for to the winbin.wtf URL to find what you are looking for.

### Scope

For now, the scope of this project is only files that come with a base install of Windows Desktop. New binaries installed by the control panel item "Turn Windows features on or off" are currently not in scope. If/when we document all regular Windows Desktop binaries, we may expand the scope at that time to servers and/or optional Windows binaries.

### Contributing

There are a huge number of built-in Windows binaries, so any contributions to this documentation would be appreciated. I've created a template that **must be** used when documenting a new binary. Modifications to the template should be discussed first by opening an issue in this repository. Adding new fields to the template will require us to retroactively modify all existing binary docs, so be prepared to make a good argument for adding a field.
