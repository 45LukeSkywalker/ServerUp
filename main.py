import subprocess
import json
with open("config.json", "r") as file:
    config = json.load(file)

serverips = config["servers"]

for ip in serverips:
    pinger = subprocess.run(["ping", ip], capture_output=True)
    if "Ping request could not find host" in pinger.stdout.decode():
        print(f"{ip}: ping failure")
    else:
        print(f"{ip}: ping success")