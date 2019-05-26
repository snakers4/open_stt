#!/usr/bin/python
from urllib import request

url = "https://ru-open-stt.ams3.digitaloceanspaces.com"

# download data
with open("md5sum.lst") as f:
    for line in f:
        file = line.split(" ")[1].rstrip()
        with open(file, "wb+") as data:
            response = request.urlopen(url + "/" + file)
            data.write(response.read())
print("Files was downloaded")
