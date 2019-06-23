#!/usr/bin/python
import hashlib
import os
from wget import download


url = "https://ru-open-stt.ams3.digitaloceanspaces.com"

# download data
with open("md5sum.lst") as f:
    for line in f:
        md5, file = line.rstrip().split(" ")
        while True:
            print(file)
            response = download(url + "/" + file)
            md5_file = hashlib.md5(open(file, "rb").read()).hexdigest()
            if md5 != md5_file:
                os.remove(file)
                print(
                    "MD5 digest for "
                    + file
                    + " is incorrect, the file will be downloaded again."
                )
            else:
                break
    print("Files was downloaded")
