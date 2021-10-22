from bs4 import BeautifulSoup

html = '''<table>
<tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr>
<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr>
<tr><td>Little Caesars</td><td>12</td><td>144</td></tr>
</table>'''

table = BeautifulSoup(html, 'html5lib')
table_rows = table.find_all(name='tr')
for i, row in enumerate(table_rows):
    print('row', i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('column', j, 'cell', cell)
