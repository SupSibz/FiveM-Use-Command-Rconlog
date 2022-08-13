import socket , json
from requests import get
import time

HOST = "0.0.0.0"
SERVERPORT = 30120
RCONPASSWORD = ""

timeset = time.time()
ip = get('https://api.ipify.org').text

while True:
    time.sleep(20)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((HOST, SERVERPORT))
    sock.send(b"\xFF\xFF\xFF\xFF"+bytes(("rcon {0} giveitem 1 phone 1 {1}"))) # Command Server giveitem 1 phone 1
    sock.close()