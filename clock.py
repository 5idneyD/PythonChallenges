import sys
import datetime as dt
import time
import os
from art import tprint

def main():
    print(chr(27) + "[2J")
    sys.stdout.flush()
    os.system("cls")
    now = dt.datetime.now().strftime("%I:%M:%S")

    units = now.split(":")
    hour, minute, second = units[0], units[1], units[2]

    current = f"{hour}:{minute}:{second}"
    tprint(current)
    time.sleep(1)
    
while True:
    main()