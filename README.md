progress-visualizations
=======================
1. Download raw osm data
	use:
	- JOSM
	- metro.teczno.com
	- http://extract.bbbike.org/?lang=en&sw_lng=-95.813&sw_lat=29.455&ne_lng=-94.868&ne_lat=30.089&format=osm.pbf&oi=1&layers=0B000000T
	- mirror download plugin in JOSM.
	- http://rub21.github.io/download-osm-data/#10.00/32.5462/-96.6347

2. run covert.py to generate geojson. 

$ python convert-nodes.py  houston2.osm houston.geojson

3. convert to sqlite via ogr2ogr.

$ ogr2ogr -f "SQLite" \
  -where " user in ( 'Rub21' )
      and timestamp >= 1382918400 
      and timestamp <= 1388793600 " \
  -nln mapathon houston.sqlite houston.geojson 

  ####stats
  $ python app.y

+--------+-----------+-----------+
|  User  | Nodes V=1 | Nodes V>1 |
+--------+-----------+-----------+
| ediyes |    1090   |    162    |
| Rub21  |    220    |     1     |
+--------+-----------+-----------+
