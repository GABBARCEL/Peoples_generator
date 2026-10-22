from _manager.Generator import *
import json
import sqlite3 #futuramente
from pathlib import Path
from datetime import datetime

def saveAsJSON_folder(peoples):     #Lembrar futuramente de adicionar endereço personalizado!
    outputPath = Path(__file__).resolve().parent.parent / "output"
    folderName = datetime.now().strftime("%Y-%m-%d|%H.%M.%S.%f.json")
    folderPath = outputPath / folderName

    with folderPath.open("x", encoding="utf-8") as JSONfolder:
        json.dump(peoples, JSONfolder, ensure_ascii=False, indent=4)

    return folderPath
