# WORKING! #
# simple code probably stolen from stack overflow to copy stuff to your clipboard

import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

copy2clip('This is on my clipboard!')
