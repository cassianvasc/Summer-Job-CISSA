# app_principal/API.py
import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCKCHAIN_PATH = os.path.join(BASE_DIR, "BLOCKCHAIN.txt")


def registrar_incidente(incidente_dict: dict):

    bloco = {
        "timestamp": datetime.now().isoformat(),
        "incidente": incidente_dict
    }

    with open(BLOCKCHAIN_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(bloco, ensure_ascii=False))
        f.write("\n")

    return True
