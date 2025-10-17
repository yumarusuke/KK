import requests

yumaru=requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001")
print(yumaru.json())