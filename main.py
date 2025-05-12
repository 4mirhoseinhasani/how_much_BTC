from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime

# Format accepted by coinmarketcap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '6ca00abd-9cd6-46bc-9851-a222e1f7d7b7',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  BTC_price = data['data']['BTC']['quote']['USD']['price']  # extract just price of bitcoin of data
  now = datetime.datetime.now()
  print(f"The price of Bitcoin on date {now.date()} and time {now.strftime("%H:%M:%S")} is: ** {BTC_price:0.4f} $ **")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)