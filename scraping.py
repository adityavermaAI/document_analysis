import requests, time, os
import pandas as pd

df = pd.read_excel("cik_list.xlsx")
file_series = (df["SECFNAME"])
# print(*(file_series[118:]), sep="\n")

for file in file_series[118:]:
    file_name = os.path.split(file)[-1]
    print("https://www.sec.gov/Archives/%s" %file)
    url = "https://www.sec.gov/Archives/%s" %file
    print(url)
    r = requests.get(url, allow_redirects=True)
    print(r.content)
    with open('%s' %file_name, 'wb')as file_obj:
        file_obj.write(r.content)
    time.sleep(0.5)
