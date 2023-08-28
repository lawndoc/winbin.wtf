---
title: msinfo32.exe
description: |
  A tool used to show system hardware, capabilities, software, drivers, and other information. This data is often used for diagnostic purposes.
file-size:
    min: "376KB"
    max: "376KB"
signature: CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
spawned-by:
    - explorer.exe
spawns:
    - None
dlls:
    - C:\WINDOWS\SYSTEM32\ntdll.dll
    - C:\WINDOWS\System32\KERNEL32.DLL
    - C:\WINDOWS\System32\KERNELBASE.dll
    - C:\WINDOWS\System32\ADVAPI32.dll
    - C:\WINDOWS\System32\msvcrt.dll
    - C:\WINDOWS\System32\sechost.dll
    - C:\WINDOWS\System32\RPCRT4.dll
    - C:\WINDOWS\System32\GDI32.dll
    - C:\WINDOWS\System32\win32u.dll
    - C:\WINDOWS\System32\gdi32full.dll
    - C:\WINDOWS\System32\msvcp_win.dll
    - C:\WINDOWS\System32\ucrtbase.dll
    - C:\WINDOWS\System32\USER32.dll
    - C:\WINDOWS\System32\OLEAUT32.dll
    - C:\WINDOWS\System32\combase.dll
    - C:\WINDOWS\System32\ole32.dll
    - C:\WINDOWS\System32\SHLWAPI.dll
    - C:\WINDOWS\System32\SETUPAPI.dll
    - C:\WINDOWS\System32\COMDLG32.dll
    - C:\WINDOWS\System32\shcore.dll
    - C:\WINDOWS\system32\MFC42u.dll
    - C:\WINDOWS\System32\SHELL32.dll
    - C:\WINDOWS\system32\ATL.DLL
    - C:\WINDOWS\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.22000.120_none_9d947278b86cc467\COMCTL32.dll
    - C:\WINDOWS\system32\POWRPROF.dll
    - C:\WINDOWS\system32\SLC.dll
    - C:\WINDOWS\System32\IMM32.DLL
lol-bin: False
gui: True
resources:
    - name: Microsoft Server Docs
      link: https://github.com/MicrosoftDocs/windowsserverdocs/blob/main/WindowsServerDocs/administration/windows-commands/msinfo32.md
acknowledgements:
    - name: Auron
      handle: mou-ikkai
---

{% include filedoc.html %}
