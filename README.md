`./data/` contains raw location data scraped from http://nd.solveninja.org/

`./output/` contains data processed  from `./data/` and converted to GeoJSONs.

`script.py` converts current data from ReapBenefit's webpage (available in `./data/`) into GeoJSON format.

`./web-app/` contains the front-end code which renders MapBox's map, and renders the processed GeoJSONs.
