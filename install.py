import os
import requests

os.system("pip install typer[all] PyGithub")
kkk = requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/main.py").text
if not os.path.exists("/cleberpkg/"):
  os.mkdir("/cleberpkg")
with open("/cleberpkg/main.py", "wt") as file:
  file.write(kkk)
with open("/cleberpkg/installed.json", "wt") as file:
  file.write("[]")
os.system("cp /cleberpkg/main.py /sbin/cleberpkg")
print("Installed cleberpkg")
