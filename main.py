import subprocess
pinger = subprocess.run(["ping", ])
pinger.stdout.decode() # Output