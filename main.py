#!/usr/bin/env python3

import requests
import json
import typer
import os
import github

app = typer.Typer()

@app.command()
def install(packagename:str):
  packages_obj = json.loads(requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/packages.json").text)
  try:
    package_obj = packages_obj[packagename]
  except:
    print("Package not found")
    return None
  with open("/cleberpkg/installed.json") as file:
    installed = json.loads(file.read())
  if packagename in installed:
    print("Package {} is already installed".format(packagename))
    return None
  deb = package_obj["deb"]
  dependencies = package_obj["dependencies"]
  for x in dependencies:
    install(x)
  print("Downloading {}".format(packagename))
  deb = requests.get(deb).content
  with open("/cleberpkg/cache.deb", "wb") as file:
    file.write(deb)
  print("Installing {}".format(packagename))
  os.system("dpkg -i /cleberpkg/cache.deb")
  installed.append(packagename)
  with open("/cleberpkg/installed.json", "wt") as file:
    file.write(json.dumps(installed))
  print("Installed {}".format(packagename))

@app.command()
def info(packagename:str):
  packages_obj = json.loads(requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/packages.json").text)
  try:
    package_obj = packages_obj[packagename]
  except:
    print("Package not found")
    return None
  name = package_obj["name"]
  description = package_obj["description"]
  dependencies = package_obj["dependencies"]
  print("Name: {}".format(name))
  print("Description: {}".format(description))
  print("Dependencies:")
  for x in dependencies:
    print(x)

@app.command()
def create():
  packages_obj = json.loads(requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/packages.json").text)
  while True:
    package_name = input("Package Name: ")
    try:
      _ = packages_obj[package_name]
      print("Package Already Exists")
    except:
      break
  pack_name = input("Name of the Package: ")
  description = input("Description: ")
  dependencies = input("Dependencies (separated by space): ").split()
  package = input("Link to the .deb file: ")
  packagee = {
    "name": pack_name,
    "description": description,
    "dependencies": dependencies,
    "deb": package
  }
  token = requests.get("https://site.batatinha-espac.repl.co/").text
  g = github.Github(token)
  repo = g.get_repo("batatinha-espacial/cleberpkg")
  file = repo.get_contents("packages.json")
  file_contents = str(file.decoded_content, "utf-8")
  contents_obj = json.loads(file_contents)
  contents_obj[package_name] = packagee
  towrite = json.dumps(contents_obj)
  repo.update_file(file.path, "Add a package", towrite, file.sha)
  print("Successfully created package {}".format(package_name))

@app.command()
def download(package_name:str):
  packages_obj = json.loads(requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/packages.json").text)
  try:
    package_obj = packages_obj[packagename]
  except:
    print("Package not found")
    return None
  deb = package_obj["deb"]
  where = input("Where to save: ")
  with open(where, "wb") as file:
    file.write(requests.get(deb).content)
  print("File saved")

@app.command()
def list():
  packages_obj = json.loads(requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/packages.json").text)
  keys = packages_obj.keys()
  where = input("Where to save: ")
  with open(where, "wt") as file:
    for x in keys:
      file.write("{}\n".format(x))
  print("List of packages saved")

@app.command()
def updatecleber():
  pyobj = requests.get("https://raw.githubusercontent.com/batatinha-espacial/cleberpkg/main/install.py").text
  with open("/cleberpkg/cache.py", "wt") as file:
    file.write(pyobj)
  os.system("sudo python3 /cleberpkg/cache.py")
  
app()
