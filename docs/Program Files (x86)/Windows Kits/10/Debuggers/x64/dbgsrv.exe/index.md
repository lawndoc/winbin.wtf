---
title: dbgsrv.exe
description: Microsoft User-Mode Debugger Process Server
file-size:
    min: "?KB"
    max: "?KB"
signature: CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
spawned-by:
    - Unknown
spawns:
    - Unknown
dlls:
    - C:\Windows\SYSTEM32\ntdll.dll
    - C:\Windows\System32\KERNEL32.DLL
    - C:\Windows\System32\KERNELBASE.dll
    - C:\Windows\System32\msvcrt.dll
    - C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbgeng.dll
    - C:\Windows\System32\ucrtbase.dll
    - C:\Windows\System32\RPCRT4.dll
    - C:\Windows\System32\bcrypt.dll
    - C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbgmodel.dll
    - C:\Windows\System32\OLEAUT32.dll
    - C:\Windows\System32\msvcp_win.dll
    - C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbghelp.dll
    - C:\Windows\SYSTEM32\XmlLite.dll
    - C:\Windows\System32\combase.dll
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
