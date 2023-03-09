import json

from plotly.graph_objs import Layout
from plotly import offline


filename = 'data/eq_data_30_day_m1.geojson'
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_text,
         'marker': {
             'size': [3*mag for mag in mags],
             'color': mags,
             'colorscale': 'Bluered',
             'reversescale': False,
             'colorbar': {'title': 'Magnitude'}
         }}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
