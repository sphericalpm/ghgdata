import matplotlib.pyplot as plt
import requests

VARIABLE = 'B3C6CE61-81BF-440C-A5EC-3451AB9205B8'
COUNTRIES = ('DEU', 'EUA', 'FRA', 'GBR', 'ITA')

url = 'http://ghg-data.s3-website.eu-central-1.amazonaws.com/{}.json'.format(VARIABLE)

vardata = requests.get(url).json()

baseyear_position = vardata['years'].index('Base Year')  # we don't need base year

del vardata['years'][baseyear_position]

for party in vardata['series']:
    if party not in COUNTRIES:
        continue
    del vardata['series'][party][baseyear_position]
    plt.plot(vardata['years'], vardata['series'][party], label=party)

plt.title('Methane Emissions in Europe Go Down')
plt.legend()
plt.xticks(rotation=70)

plt.show()
