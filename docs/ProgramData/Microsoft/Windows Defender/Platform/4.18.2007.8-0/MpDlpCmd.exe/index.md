---
title: MpDlpCmd.exe
description: Microsoft Malware Protection DLP Command Line Utility
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
    - C:\Windows\System32\ADVAPI32.dll
    - C:\Windows\System32\msvcrt.dll
    - C:\Windows\System32\sechost.dll
    - C:\Windows\System32\RPCRT4.dll
    - C:\Windows\System32\ucrtbase.dll
    - C:\Windows\System32\combase.dll
    - C:\Windows\System32\bcryptPrimitives.dll
    - C:\Windows\System32\USER32.dll
    - C:\Windows\System32\win32u.dll
    - C:\Windows\System32\GDI32.dll
    - C:\Windows\System32\gdi32full.dll
    - C:\Windows\System32\msvcp_win.dll
    - C:\Windows\SYSTEM32\UxTheme.dll
    - C:\Windows\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.17763.1518_none_de6e2bd0534e2567\COMCTL32.dll
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
