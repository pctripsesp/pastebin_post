import requests
import ast

#GET LIST LIKE: [['link1','https://pastebin.com/...'],['link2','https://pastebin.com/...'],['link3','https://...']]
response = requests.get('https://pastebin.com/raw/FfE2...')   #EXAMPLE
data = response.text                                          #use "data = response.json" if its JSON format raw
links = ast.literal_eval(data)

print("En total hay", len(links),"links")
for link in links:
    print(link)
