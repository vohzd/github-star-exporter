import json
import subprocess

file = open("star.json", encoding='utf-8-sig')
data = json.load(file)

for key in data:
    subprocess.call(["git", "clone", key["clone_url"]])
