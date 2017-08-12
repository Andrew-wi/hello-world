import parse as p

import geojson

def create_map(data_file):
    # define the type of GeoJSON we're creating
    geo_map = {'type': 'FeatureCollection'}

    # define empty list ot collect each point to graph
    item_list = []

    # iterate over our data to create GeoJSON document.
    # we're using enumerate() so we get the line, as well
    # as the index, which is the line number
    for index, line in enumerate(data_file):

        # skip any zero cordinates as this will throw off
        # our map.
        if line['X'] == '0' or line['Y'] == '0':
            continue

        # setup a new dictionary for each iteration
        data = {}

        # assign line items to appropriate GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {  'desription': line['Descript'],
                                'title': line['Category'],
                                'date': line['Date']}
        data['geometry'] = {    'type': 'Point',
                                'coordinates': (line['X'], line['Y'])}

        # add data dictionary to our item_list
        item_list.append(data)

    # for each point in our item_list, we add the point to our
    # dictionary. setdefault creates a key called 'features' that
    # has a value type of an empty list. With each iteration, we
    # are appending our point to that list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # now that all data is parsed in GeoJSON write to a file so we
    # can upload it to gist.github.com
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.MY_FILE, ",")

    create_map(data)

if __name__ == "__main__":
    main()
