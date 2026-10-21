"""
#Import os Library
import os

# Create Directory
#os.mkdir("direc")


"Test"
#os.chdir("C:\Windows\System32")
#print("Current directory now:" , os.getcwd())
#os.mkdir("direc")
print (os.chroot("/test/user"))
"""

"""The key is :
ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    """

import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Relance le script avec élévation UAC
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
else:
    print("Exécution avec privilèges administrateur !")
    # Ton code privilégié ici
