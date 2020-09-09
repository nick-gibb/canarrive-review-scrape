from google_play_scraper import reviews_all
import json

result = reviews_all(
    'ca.gc.cbsa.coronavirus',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

for i in result:
    if i.get('repliedAt', 0):
        i['repliedAt'] = i['repliedAt'].strftime("%m/%d/%Y, %H:%M:%S")
    if i.get('at', 0):
        i['at'] = i['at'].strftime("%m/%d/%Y, %H:%M:%S")


with open('google.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)