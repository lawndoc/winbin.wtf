#!/usr/bin/env python3
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")
rootdir = os.getcwd()

with open(f"{rootdir}/docs/Windows/index.md", "r") as f:
    content = f.read()

for subdir, dirs, files in os.walk(rootdir):
    for directory in dirs:
        if directory.lower().endswith(".dll") or directory.lower().endswith(".exe"):
            pass
        elif os.path.exists(f"{subdir}/{directory}/index.md"):
            pass
        else:
            with open(f"{subdir}/{directory}/index.md", "w") as f:
                f.write(content)
