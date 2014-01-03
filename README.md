progress-visualizations
=======================
# Dowload for data for all Users
1. Download raw osm data
	use:
	- JOSM
	- metro.teczno.com
	- http://extract.bbbike.org/?lang=en&sw_lng=-95.813&sw_lat=29.455&ne_lng=-94.868&ne_lat=30.089&format=osm.pbf&oi=1&layers=0B000000T
	- mirror download plugin in JOSM.
	
2. run covert.py to generate geojson. 

			$ $ python convert-nodes.py jacksonville_all_users.osm jacksonville_all_users.geojson

3. convert to sqlite via ogr2ogr. 

- Para 2  usuarios especifico , ediyes, Rub21

	date:
	- 01/03/2014 = 1388707200
	-01/04/2014 = 1388793600

			$ ogr2ogr -f "SQLite" \
			  -where " user in ( 'ediyes','Rub21' )
			      and timestamp >= 1388707200 
			      and timestamp <= 1388793600 " \
			  -nln mapathon jacksonville_all_users.sqlite jacksonville_all_users.geojson 

- Para todos lo usuarios

			$ ogr2ogr -f "SQLite"  -nln mapathon jacksonville_all_users2.sqlite jacksonville_all_users.geojson

4. estadisticas
	
	* Especifico para dos usuarios: *

  			$ python stats.py jacksonville_all_users.sqlite

			+--------+-----------+-----------+
			|  User  | Nodes V=1 | Nodes V>1 |
			+--------+-----------+-----------+
			| ediyes |    2310   |    306    |
			| Rub21  |    220    |     1     |
			+--------+-----------+-----------+

	* Para todos los usuarios * 
			$ python stats.py jacksonville_all_users2.sqlite

			+------------------------+-----------+-----------+
			|          User          | Nodes V=1 | Nodes V>1 |
			+------------------------+-----------+-----------+
			|        jumbanho        |   57050   |     66    |
			|    woodpeck_fixbot     |     0     |    9395   |
			|        TIGERcnl        |    3780   |     0     |
			|         ediyes         |    3420   |    326    |
			|          dcat          |    1039   |     2     |
			|       osmmapper        |    475    |    561    |
			|          NE2           |    705    |     58    |
			|         zephyr         |    643    |     3     |
			|         sadam          |    399    |     0     |
			|      Aaron Lidman      |    317    |     63    |
			|         ToeBee         |     0     |    371    |
			|         Rub21          |    220    |     1     |
			|       tscofield        |     92    |     0     |
			|       davidearl        |     0     |     85    |
			|        Geogast         |     0     |     58    |
			|       pschonmann       |     34    |     22    |
			|        iandees         |     49    |     0     |
			| OSMF Redaction Account |     0     |     38    |
			|        Evanator        |     4     |     24    |
			|        amillar         |     12    |     0     |
			|       MurrietaCR       |     11    |     0     |
			|      Hundehalter       |     2     |     4     |
			|      RetiredInNH       |     2     |     0     |
			|       RussNelson       |     2     |     0     |
			|     Alex W Rickard     |     1     |     0     |
			|          J_W           |     0     |     1     |
			|     RichardCorbin      |     0     |     1     |
			|       andrewpmk        |     0     |     1     |
			|    goodWaldohunting    |     0     |     1     |
			|     oddityoverseer     |     0     |     1     |
			|         xybot          |     0     |     1     |
			+------------------------+-----------+-----------+


# Dowload osm data for two specific user

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

