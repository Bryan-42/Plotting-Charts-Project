import plotly.express as px
import csv

rows = []

with open("final.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

star_masses = []
star_radiuses = []

for star_data in star_data_rows:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[4])

fig = px.scatter(x = star_radiuses, y = star_masses)
fig.show()