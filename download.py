import os
import hashlib
from wget import download


url = "https://azureopendatastorage.blob.core.windows.net/openstt/ru_open_stt_opus/"

with open("md5sum.lst") as f:
    for line in f:
        md5, file = line.rstrip().split(" ")
        while True:
            print("\n" + file)
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
