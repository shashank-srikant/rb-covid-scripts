`./data/` contains raw location data scraped from http://nd.solveninja.org/. Data as of 7AM, 5 April, IST.

|File   |# of data points   |
|---|---|
| Citizen ease  | 181  |
| Medical services  | 65  |
| People needing help  |  109 |
| Places supporting needy  |  812 |
| Social distancing  | 68  |
| Volunteer  | 37  |
| **Total**  | **1273**  |

`./output/` contains data processed  from `./data/` and converted to GeoJSONs.

`script.py` converts current data from ReapBenefit's webpage (available in `./data/`) into GeoJSON format.

`./web-app/` contains the front-end code which renders MapBox's map, and renders the processed GeoJSONs.
