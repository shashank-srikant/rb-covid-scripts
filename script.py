from os import listdir
from os.path import isfile, join
import json

mypath = './data/'
outpath = './output/'
jsonfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for j in jsonfiles:
    with open(mypath+j, 'r') as f:
        obj = json.load(f)
    
    feature_list = list()
    for i in obj['data']:
        per_point_dict, prperties = dict(), dict()
        for k, v in i.items():
            # print(k)
            # print(v)
            if not(k == 'lat' or k == 'lng'):
                prperties[k] = v
        long_lat = [float(i['lng']), float(i['lat'])]

        per_point_dict["geometry"] = {"type": "Point", "coordinates": long_lat}
        per_point_dict["properties"] = prperties
        per_point_dict["type"] = "Feature"
        feature_list.append(per_point_dict)

    final_dict = {}
    final_dict["type"] = "FeatureCollection"
    final_dict["crs"] = {"type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }}
    final_dict["features"] = feature_list

    with open(outpath+j,'w') as f:
        json.dump(final_dict, f)

    # print(final_dict)
    