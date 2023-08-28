---
title: MpCmdRun.exe
description: Microsoft Malware Protection Command Line Utility
file-size:
    min: "?KB"
    max: "?KB"
signature: CN=Microsoft Windows Publisher, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
spawned-by:
    - Unknown
spawns:
    - Unknown
dlls:
    - C:\Windows\SYSTEM32\ntdll.dll
    - C:\Windows\System32\KERNEL32.DLL
    - C:\Windows\System32\KERNELBASE.dll
    - C:\Windows\System32\ucrtbase.dll
    - C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\mpclient.dll
    - C:\Windows\System32\ADVAPI32.dll
    - C:\Windows\System32\msvcrt.dll
    - C:\Windows\System32\sechost.dll
    - C:\Windows\System32\RPCRT4.dll
    - C:\Windows\system32\version.dll
    - C:\Windows\System32\combase.dll
    - C:\Windows\System32\bcryptPrimitives.dll
    - C:\Windows\System32\kernel.appcore.dll
    - C:\Windows\System32\USER32.dll
    - C:\Windows\System32\win32u.dll
    - C:\Windows\System32\GDI32.dll
    - C:\Windows\System32\gdi32full.dll
    - C:\Windows\System32\msvcp_win.dll
    - C:\Windows\System32\IMM32.DLL
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
