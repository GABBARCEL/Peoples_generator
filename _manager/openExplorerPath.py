import os
import subprocess
import sys
from _manager.config import outputPath


# Novamente, me parece mais certo usar uma variável local do que global. (mas sinto que isso está bem errado também, mas que se dane)
output = outputPath

def openExplorer(path = output):
    if sys.platform == "win32":
        os.startfile(path)

    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])

    else:
        subprocess.Popen(["xdg-open", path])

