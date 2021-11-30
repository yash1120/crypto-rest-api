from bs4 import BeautifulSoup 
import requests
from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

url ='https://goldprice.org/cryptocurrency-price'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content,"html.parser")
table = soup.find('table',class_="views-table cols-8 table table-striped table-hover table-condensed table-0")
lists = table.find_all('tr')
lists =lists[1:]

crypto ={}
for li in lists:
    name = li.find('td',class_="views-field views-field-field-crypto-proper-name").text.strip()
    market_cap = li.find('td',class_="views-field views-field-field-market-cap views-align-right hidden-xs").text.strip()
    price = li.find('td',class_="views-field views-field-field-crypto-price views-align-right").text.strip()
    supply = li.find('td',class_="views-field views-field-field-crypto-circulating-supply views-align-right").text.strip()
    volume = li.find('td',class_="views-field views-field-field-crypto-volume views-align-right hidden-xs").text.strip()
    change= li.find('td',class_="views-field views-field-field-crypto-price-change-pc-24h views-align-right").text.strip()

    crypto[name]={"Market Cap":market_cap, "Price":price,"Supply":supply,"Volume":volume,"24hr change": change}

class AllCrypto(Resource):
    def get(self):
        url ='https://goldprice.org/cryptocurrency-price'
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.content,"html.parser")
        table = soup.find('table',class_="views-table cols-8 table table-striped table-hover table-condensed table-0")
        lists = table.find_all('tr')
        lists =lists[1:]

        crypto ={}
        for li in lists:
            name = li.find('td',class_="views-field views-field-field-crypto-proper-name").text.strip()
            market_cap = li.find('td',class_="views-field views-field-field-market-cap views-align-right hidden-xs").text.strip()
            price = li.find('td',class_="views-field views-field-field-crypto-price views-align-right").text.strip()
            supply = li.find('td',class_="views-field views-field-field-crypto-circulating-supply views-align-right").text.strip()
            volume = li.find('td',class_="views-field views-field-field-crypto-volume views-align-right hidden-xs").text.strip()
            change= li.find('td',class_="views-field views-field-field-crypto-price-change-pc-24h views-align-right").text.strip()

            crypto[name]={"Market Cap":market_cap, "Price":price,"Supply":supply,"Volume":volume,"24hr change": change}
        return crypto
class Crypto(Resource):
    def get(self,cname):
        return crypto[cname]
api.add_resource(AllCrypto,"/api/all")
api.add_resource(Crypto,"/api/<string:cname>")
if __name__=="__main__":
    app.run(debug=True)