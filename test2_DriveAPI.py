import json
import requests

headers = {"Authorization": "Bearer ya29.Il-9B1nMVogq1pz8045P1WT0sFzXClnh_Ba3eurwORa2ewR-mRZNFGx7HdayOneWHerzmqRGJ0EppjphzdStnFS2HURzBHwlprGoHQjwqIkgANSmB5J4VtOTjtyGrMbvWA"}

para = {
    "name": "test1.txt",
    "parents": ["1P7Uuh0x09aUsPOhOyJxKW9fGA2utPiXC"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./test1.txt", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
