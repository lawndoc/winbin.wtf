---
title: systemreset.exe
description: |
  The executable used for resetting the Windows OS back to a fresh install, with the option to keep files or reset everything to default. The program can be opened using Settings, running it in the System32 folder, or typing 'systemreset' in Command Prompt.
file-size:
    min: "508KB"
    max: "508KB"
signature: Microsoft Windows
spawned-by:
    - explorer.exe
	- SystemSettings.exe
    - cmd.exe
spawns:
    - none
dlls:
    - Unknown
lol-bin: False
resources:
    - name: No Reliable Source
      link:
acknowledgements:
    - name: Auron
      handle: mou-ikkai
---

{% include filedoc.html %}
