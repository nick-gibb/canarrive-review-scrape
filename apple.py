import json
from app_store_scraper import AppStore

arrivecan = AppStore(country="ca", app_name="arrivecan")
arrivecan.review()
for i in arrivecan.reviews:
    i['date'] = i['date'].strftime("%m/%d/%Y, %H:%M:%S")

with open('apple.json', 'w', encoding='utf-8') as f:
    json.dump(arrivecan.reviews, f, ensure_ascii=False, indent=4)