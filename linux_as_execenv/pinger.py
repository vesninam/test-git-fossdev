import requests
from datetime import datetime, timedelta

url_template = "https://simurg.space/gen_file?data=obs&date={date}"

now = datetime.now()
date_str = now.strftime("%Y-%m-%d") 
print(f"Current datetime is {now} and date {date_str}")

url = url_template.format(date=date_str)

response = requests.get(url=url, stream=True)
print(f"From url {url} got {response}")


