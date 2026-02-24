import requests

url_template = "https://simurg.space/gen_file?data=obs&date={date}"
url = url_template.format(date="2026-02-20")

response = requests.get(url=url, stream=True)
print(f"From url {url} got {response}")


