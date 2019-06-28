import sys, os
import subprocess
"""This is a way for me to generate the url needed for posting the videos to the 
FreeCAD forum boards.  In Windows 10 Explorer I'm able to drag and drop the webm video to
this file, which then creates the url and video tags string, and then copies it to the clipboard.

This greatly improves things because now I don't have to go to github.com each time to get the url.
"""

def modifyThineSelf():
    """This is just to modify the file so it appears at the top of the folder when sorting by modified date."""
    fin = open(__file__, 'r')
    code = fin.read()
    fin.close()
    fout = open(__file__, 'w')
    fout.write(code)
    fout.close()

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

prepend = "https://raw.githubusercontent.com/mwganson/FreeCAD-videos/master/"

if len(sys.argv) != 2:
    input("Please drag and drop a file or enter filename as command line parameter")
else:
    modifyThineSelf()
    fileName = os.path.basename(sys.argv[1])
    data = "[video]" + prepend + fileName + "[/video]"
    copy2clip(data)

    #Following could be removed as it only pauses the screen and displays the confirmation
    text = input(data + " has been copied to clipboard (press enter to close) ")


