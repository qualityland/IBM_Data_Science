import requests
import pandas as pd

url = "https://api.spacexdata.com/v4/launches/past"
resp = requests.get(url)
data = pd.json_normalize(resp.json())
print(data)
