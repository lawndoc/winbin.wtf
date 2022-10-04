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
    - C:\Windows\System32\advapi32.dll
    - C:\Windows\System32\APMon.dll
    - C:\Windows\System32\AppMon.dll
    - C:\Windows\System32\BCP47Langs.dll
    - C:\Windows\System32\bcrypt.dll
    - C:\Windows\System32\bcryptprimitives.dll
    - C:\Windows\System32\bidispl.dll
    - C:\Windows\System32\cfgmgr32.dll
    - C:\Windows\System32\clbcatq.dll
    - C:\Windows\System32\combase.dll
    - C:\Windows\System32\crypt32.dll
    - C:\Windows\System32\cryptbase.dll
    - C:\Windows\System32\cryptsp.dll
    - C:\Windows\System32\cscapi.dll
    - C:\Windows\System32\devobj.dll
    - C:\Windows\System32\devrtl.dll
    - C:\Windows\System32\dhcpcsvc.dll
    - C:\Windows\System32\dhcpcsvc6.dll
    - C:\Windows\System32\dnsapi.dll
    - C:\Windows\System32\drvstore.dll
    - C:\Windows\System32\dsrole.dll
    - C:\Windows\System32\DWrite.dll
    - C:\Windows\System32\FWPUCLNT.DLL
    - C:\Windows\System32\FXSMON.dll
    - C:\Windows\System32\FXSRESM.dll
    - C:\Windows\System32\gdi32.dll
    - C:\Windows\System32\gdi32full.dll
    - C:\Windows\System32\gpapi.dll
    - C:\Windows\System32\iertutil.dll
    - C:\Windows\System32\inetpp.dll
    - C:\Windows\System32\IPHLPAPI.DLL
    - C:\Windows\System32\kernel.appcore.dll
    - C:\Windows\System32\kernel32.dll
    - C:\Windows\System32\KernelBase.dll
    - C:\Windows\System32\localspl.dll
    - C:\Windows\System32\msasn1.dll
    - C:\Windows\System32\msvcp_win.dll
    - C:\Windows\System32\msvcrt.dll
    - C:\Windows\System32\mswsock.dll
    - C:\Windows\System32\msxml6.dll
    - C:\Windows\System32\msxml6r.dll
    - C:\Windows\System32\spool\drivers\x64\3\mxdwdrv.dll
    - C:\Windows\System32\netprofm.dll
    - C:\Windows\System32\netutils.dll
    - C:\Windows\System32\npmproxy.dll
    - C:\Windows\System32\nsi.dll
    - C:\Windows\System32\ntdll.dll
    - C:\Windows\System32\ntmarta.dll
    - C:\Windows\System32\ole32.dll
    - C:\Windows\System32\oleaut32.dll
    - C:\Windows\System32\OpcServices.dll
    - C:\Windows\System32\powrprof.dll
    - C:\Windows\System32\PrinterCleanupTask.dll
    - C:\Windows\System32\PrintIsolationProxy.dll
    - C:\Windows\System32\rasadhlp.dll
    - C:\Windows\System32\rpcrt4.dll
    - C:\Windows\System32\rsaenh.dll
    - C:\Windows\System32\sechost.dll
    - C:\Windows\System32\setupapi.dll
    - C:\Windows\System32\sfc_os.dll
    - C:\Windows\System32\SHCore.dll
    - C:\Windows\System32\shlwapi.dll
    - C:\Windows\System32\snmpapi.dll
    - C:\Windows\System32\spfileq.dll
    - C:\Windows\System32\spinf.dll
    - C:\Windows\System32\spoolss.dll
    - C:\Windows\System32\srvcli.dll
    - C:\Windows\System32\sspicli.dll
    - C:\Windows\System32\taskschd.dll
    - C:\Windows\System32\tcpmon.dll
    - C:\Windows\System32\spool\drivers\x64\3\tsprint.dll
    - C:\Windows\System32\ucrtbase.dll
    - C:\Windows\System32\umpdc.dll
    - C:\Windows\System32\urlmon.dll
    - C:\Windows\System32\usbmon.dll
    - C:\Windows\System32\user32.dll
    - C:\Windows\System32\userenv.dll
    - C:\Windows\System32\version.dll
    - C:\Windows\System32\win32spl.dll
    - C:\Windows\System32\win32u.dll
    - C:\Windows\System32\winhttp.dll
    - C:\Windows\System32\winnsi.dll
    - C:\Windows\System32\spool\prtprocs\x64\winprint.dll
    - C:\Windows\System32\winspool.drv
    - C:\Windows\System32\winsta.dll
    - C:\Windows\System32\wintrust.dll
    - C:\Windows\System32\ws2_32.dll
    - C:\Windows\System32\wsnmp32.dll
    - C:\Windows\System32\wtsapi32.dll
    - C:\Windows\System32\xmllite.dll
    - C:\Windows\System32\xpspushlayer.dll
    - C:\Windows\System32\xpsservices.dll
lol-bin: False
resources:
    - name: Print Spooler Microsoft Docs
      link: https://docs.microsoft.com/en-us/windows/win32/printdocs/print-spooler
acknowledgements:
    - name: C.J. May
      handle: lawndoc
    - name: Auron
      handle: mou-ikkai
---

{% include filedoc.html %}
