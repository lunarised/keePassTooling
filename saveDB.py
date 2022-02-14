import subprocess
import os
import json

test = input("This is a remote save. Type \"Confirm\" to continue \n")
if test != "Confirm":
    exit()
cwd = os.path.dirname(os.path.realpath(__file__)) 
with open("paths.json", "r") as read_file:
    data = json.load(read_file)
localPath = data["local"]["localPath"]
remotePath = data["remote"]["remotePath"]
user = data["remote"]["username"]
remoteHost = data["remote"]["remoteHost"]
p = subprocess.Popen(f'scp {localPath} {user}@{remoteHost}:{remotePath}', shell=True, cwd=cwd)
sts = p.wait()
input("Save done")
