---
title: SenseNdr.exe
description: Windows Defender Advanced Threat Protection - Sense NDR module
file-size:
    min: "?KB"
    max: "?KB"
signature: CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
spawned-by:
    - Unknown
spawns:
    - Unknown
dlls:
    - C:\Windows\SYSTEM32\ntdll.dll
    - C:\Windows\System32\KERNEL32.DLL
    - C:\Windows\System32\KERNELBASE.dll
    - C:\Windows\System32\msvcp_win.dll
    - C:\Windows\System32\ucrtbase.dll
    - C:\Windows\System32\combase.dll
    - C:\Windows\System32\RPCRT4.dll
    - C:\Windows\System32\CRYPT32.dll
    - C:\Windows\System32\WS2_32.dll
    - C:\Windows\System32\sechost.dll
lol-bin: Unknown
gui: Unknown
resources:
    - None
acknowledgements:
    - name: Strontic
      handle: strontic
    - name: C.J. May
      handle: lawndoc
---

{% include filedoc.html %}
