---
title: svchost.exe
description: |
  Windows uses svchost.exe to run system services. Services are grouped into many individual svchost.exe processes to improve reliability in case one service crashes. The system services running in SvcHost are DLL (dynamic link library) files.
  
  The first time that a SvcHost process is launched with a specific parameter, it looks for a value of the same name under the 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost' key, which it interprets as a list of service names.
file-size:
    min: "59KB"
    max: "59KB"
signature: Microsoft Windows Publisher
spawned-by:
    - C:\Windows\System32\services.exe
spawns:
    - C:\Windows\System32\taskhostw.exe
    - C:\Windows\System32\sihost.exe
dlls:
    - C:\Windows\System32\psmsrv.dll
    - C:\Windows\System32\rpcss.dll
    - C:\Windows\System32\SystemEventsBrokerServer.dll
    - C:\Windows\System32\umpnpmgr.dll
    - C:\Windows\System32\umpo.dll
    - many more to be documented...
lol-bin: False
resources:
    - name: Wikipedia
      link: https://en.wikipedia.org/wiki/Svchost.exe
acknowledgements:
    - name: C.J. May
      handle: lawndoc
---

{% include filedoc.html %}
