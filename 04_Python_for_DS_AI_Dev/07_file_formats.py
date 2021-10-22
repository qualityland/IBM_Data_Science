import pandas as pd
import json
import xml.etree.ElementTree as etree

# csv
file = 'FileExample.csv'
df = pd.read_csv(file)
# add header
df.columns = ['Name', 'Phone Number', 'Birthday']

# json
with open('filesample.json', 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)

# xml
tree = etree.parse('fileExample.xml')
root = tree.getroot()
columns = ['Name', 'Phone Number', 'Birthday']
df = pd.DataFrame(columns = columns)

for node in root:
    name = node.find('name').text
    phonenumber = node.find('phonenumber').text
    birthday = node.find('birthday').text

    df.append(pd.Series([name, phonenumber, birthday], index = columns), ignore_index = True)
