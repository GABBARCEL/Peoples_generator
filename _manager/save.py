from _manager.Generator import *
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from _manager.config import outputPath

# Usei assim, porque me parece mais certo usar uma variável local do que global. (acho que sou burro)
output = outputPath

def saveAsJSON_folder(peoples):     # Lembrar futuramente de adicionar endereço personalizado!
    folderName = datetime.now().strftime("%Y-%m-%d|%H.%M.%S.%f.json")
    folderPath = output / "JSON_lists" / folderName
    folderPath.parent.mkdir(parents=True, exist_ok=True)

    with folderPath.open("x", encoding="utf-8") as JSONfolder:
        json.dump(peoples, JSONfolder, ensure_ascii=False, indent=4)

    return folderPath

def saveAsDB_folder(peoples):
    folderName = datetime.now().strftime("%Y-%m-%d|%H.%M.%S.%f.db")
    folderPath = output / "DB_lists" / folderName
    folderPath.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(peoples, dict):
        people = [peoples]
    elif isinstance(peoples, list):
        people = peoples
    else:
        raise TypeError("peoples must be a person dictionary or a list of person dictionaries")

    columns = (
        "id",
        "nome",
        "sobrenome",
        "sexo",
        "nascimento",
        "CPF",
        "RG",
        "Estado",
        "cidade",
        "email",
        "telefone",
    )
    placeholders = ", ".join("?" for _ in columns)
    insert_sql = (
        f"INSERT INTO pessoas ({', '.join(columns)}) "
        f"VALUES ({placeholders})"
    )

    with sqlite3.connect(folderPath) as db:
        db.execute("""
            CREATE TABLE pessoas (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                sexo TEXT NOT NULL,
                nascimento TEXT NOT NULL,
                CPF TEXT NOT NULL,
                RG TEXT NOT NULL,
                Estado TEXT NOT NULL,
                cidade TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)

        rows = []
        for person in people:
            if not isinstance(person, dict):
                raise TypeError("each person must be a dictionary")

            missing = set(columns) - person.keys()
            extra = person.keys() - set(columns)
            if missing or extra:
                raise ValueError(
                    f"person fields do not match the expected format "
                    f"(missing: {sorted(missing)}, extra: {sorted(extra)})"
                )

            rows.append(
                tuple(
                    json.dumps(person[column], ensure_ascii=False)
                    if column == "sobrenome"
                    else person[column]
                    for column in columns
                )
            )

        db.executemany(insert_sql, rows)

    return folderPath

