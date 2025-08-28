# THIS SCRIPT DOWNLOADS A FILE AT YOUR DESKTOP

import requests as r
import os


def getDesktop() -> str:
    user = os.path.expanduser("~")
    desktop = os.path.join(user, "OneDrive", "Desktop")

    if os.path.exists(desktop):
        return desktop


response = r.get("https://randomfox.ca/floof")
fox = response.json()  # Dictionary
url = fox['image']  # url of image

data_url = r.get(url).content  # Downloads image

with open(os.path.join(getDesktop(), "fox.png"), "wb") as f:
    f.write(data_url)

print(f"IMAGE: {url}\nThe image is downloaded in: {getDesktop()}.")
