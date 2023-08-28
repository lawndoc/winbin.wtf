---
title: systemreset.exe
description: |
  The executable used for resetting the Windows OS back to a fresh install, with the option to keep files or reset everything to default. The program can be opened using Settings, running it in the System32 folder, or typing systemreset in Command Prompt.
file-size:
    min: "508KB"
    max: "508KB"
signature: CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
spawned-by:
    - explorer.exe
spawns:
    - none
dlls:
    - C:\WINDOWS\SYSTEM32\ntdll.dll
    - C:\WINDOWS\System32\KERNEL32.DLL
    - C:\WINDOWS\System32\KERNELBASE.dll
    - C:\WINDOWS\System32\ADVAPI32.dll
    - C:\WINDOWS\System32\msvcrt.dll
    - C:\WINDOWS\System32\sechost.dll
lol-bin: False
gui: True
resources:
    - None
acknowledgements:
    - name: Auron
      handle: mou-ikkai
    - name: Strontic
      handle: strontic
    - name: C.J. May
      handle: lawndoc
---

{% include filedoc.html %}
