---
title: spoolsv.exe
description: |
  The Windows print spooler service is used to manage the printing process. This includes retrieving the location of the correct printer driver, loading that driver, spooling high-level function calls into a print job, scheduling the print job for printing, and so on.
  
  The spooler is loaded at system startup and continues to run until the operating system is shut down.
file-size:
    min: "808KB"
    max: "808KB"
signature: No Signer
spawned-by:
    - C:\Windows\System32\services.exe
spawns:
    - C:\Windows\splwow64.exe
    - C:\Windows\System32\msiexec.exe
    - C:\Windows\System32\net.exe
    - C:\Windows\System32\regsvr32.exe
    - C:\Windows\System32\route.exe
    - C:\Windows\System32\spoolsv.exe
dlls:
    - none
lol-bin: False
resources:
    - name: Print Spooler Microsoft Docs
      link: https://docs.microsoft.com/en-us/windows/win32/printdocs/print-spooler
acknowledgements:
    - name: C.J. May
      handle: lawndoc
---

{% include filedoc.html %}
