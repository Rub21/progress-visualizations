progress-visualizations
=======================
# Download for data for all Users
1. Download raw osm data
	use:
	- JOSM
	- metro.teczno.com
	- http://extract.bbbike.org/?lang=en&sw_lng=-95.813&sw_lat=29.455&ne_lng=-94.868&ne_lat=30.089&format=osm.pbf&oi=1&layers=0B000000T
	- mirror download plugin in JOSM.
	
2. run covert.py to generate geojson. 

			$ python convert-nodes.py jacksonville_all_users.osm jacksonville_all_users.geojson

3. convert to sqlite via ogr2ogr. 

- Para 2  usuarios especifico , ediyes, Rub21

	date:
	- 01/03/2014 = 1388707200
	- 01/04/2014 = 1388793600

			$ ogr2ogr -f "SQLite" -where " user in ( 'ediyes','Rub21' )  and timestamp >= 1388707200  and timestamp <= 1388793600 "  -nln mapathon jacksonville_all_users.sqlite jacksonville_all_users.geojson 

- Para todos lo usuarios

			$ ogr2ogr -f "SQLite"  -nln mapathon jacksonville_all_users2.sqlite jacksonville_all_users.geojson

4. estadisticas
	
	* Especifico para dos usuarios: *

  			$ python stats.py jacksonville_all_users.sqlite

			+--------+-----------+-----------+
			|  User  | Nodes V=1 | Nodes V>1 |
			+--------+-----------+-----------+
			| ediyes |    2310   |    306    |
			| Rub21  |    217    |     1     |
			+--------+-----------+-----------+

# Download osm data for two specific user

1. Download raw osm data

	use:  http://rub21.github.io/download-osm-data/#11.00/34.7520/-77.4506

2. run covert.py to generate geojson. 

		$ python convert-nodes.py jacksonville_2_users.osm jacksonville_2_users.geojson

3. convert to sqlite via ogr2ogr. 

			$ ogr2ogr -f "SQLite"  -nln mapathon jacksonville_2_users.sqlite jacksonville_2_users.geojson

si necesitamos especificar la feha

			$ ogr2ogr -f "SQLite"  -where "timestamp >= 1388707200 and timestamp <= 1388793600 " -nln mapathon jacksonville_2_users.sqlite jacksonville_2_users.geojson

4. estadisticas

			$ python stats.py jacksonville_2_users.sqlite
			+--------+-----------+-----------+
			|  User  | Nodes V=1 | Nodes V>1 |
			+--------+-----------+-----------+
			| ediyes |    4467   |    583    |
			| Rub21  |    207    |     1     |
			+--------+-----------+-----------+

