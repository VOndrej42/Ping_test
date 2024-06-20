import subprocess
import time
from datetime import datetime
import re
import logging

# Nastaveni logovani
logging.basicConfig(filename="log.txt", format="%(message)s", level=logging.INFO)

# Vytvoreni loggeru
logger = logging.getLogger(__name__)


while True:

    # Spustí příkaz ping v cmd a výstup uloží výstup do proměnné 'output'
    output = subprocess.Popen(['cmd', '/c', 'ping 8.8.8.8 -n 1',], stdout=subprocess.PIPE).communicate()[0].decode()
    output = output.split(" ")[10]
    
    # Regular Expression - regulární výraz v podmínce pro ověření, zda na výstupu dostávám opravdu hodnotu ping nebo je něco špatně
    pattern = r"^time"
    if re.match(pattern, output):
        output += (" -> Network is online")
    else:
        output += (" -> Network error or long time")
        hodnota = f"{datetime.now()} -> Network error"
        logger.info(hodnota)

    # Vytiskne výstup
    print(f"{datetime.now()} {output}")

    # Pauza před dalším opakováním
    time.sleep(1)