import requests

res = requests.get('https://www.hishcodes.com/')
res.raise_for_status()
playFile = open("saved_site.html", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()