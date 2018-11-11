import requests
import json

def getImages(coords):
    """
    Returns the data of both sidewalks
    :param lat: latitude of current coordinate
    :param long: longitude of the coordinate
    :param heading: heading of current road
    :return: returns two images of the sidewalk on either side hopefully
    """
    LOCATION = str(coords[0])+ "," + str(coords[1])
    URL="https://maps.googleapis.com/maps/api/streetview"
    PARAMS={
        "key": "AIzaSyBs24HTnH1WZsVzaDQQsIGeGXLkDtse1vM",
        "location": LOCATION,
        "size": "800x400",
        "fov": "120"
    }
    data = requests.get(url = URL, params = PARAMS)
    print(data.url)
    if data.status_code == 200:
        with open("./images/"+LOCATION+".jpg", 'wb') as f:
            f.write(data.content)

def getRoadImages(startpoint, endpoint):
    """
    Go through points with in start to end
    :param startpoint: startingpoint
    :param endpoint: endpoint of the road
    :return: return all images possible
    """
    URL = "https://roads.googleapis.com/v1/snapToRoads"
    PARAMS = {
        "key": "AIzaSyBs24HTnH1WZsVzaDQQsIGeGXLkDtse1vM",
        "path": str(startpoint[0]) + "," + str(startpoint[1]) + "|" + str(endpoint[0]) + "," + str(endpoint[1]),
        "interpolate": "true"
    }
    data = requests.get(url=URL, params=PARAMS)
    coordinates = []
    parsed = json.loads(data.text)
    for locations in parsed["snappedPoints"]:
        coordinates+=[[float(locations["location"]["latitude"]), float(locations["location"]["longitude"])]]
    for i in range(len(coordinates)):
        getImages(coordinates[i])


def parseStreetToCoordinates(start, end):
    """

    :return:
    """
    url = "https://maps.googleapis.com/maps/api/directions/json"
    querystring = {
        "key": "AIzaSyBs24HTnH1WZsVzaDQQsIGeGXLkDtse1vM",
        "origin": str(start),
        "destination": str(end)
    }
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "6d2a0d31-403a-423e-abf7-b8f5a9df403e"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    getRoadImages([float(parsed['routes'][0]["legs"][0]['start_location']['lat']), float(parsed['routes'][0]['legs'][0]['start_location']['lng'])], [float(parsed['routes'][0]["legs"][0]['end_location']['lat']), float(parsed['routes'][0]['legs'][0]['end_location']['lng'])])

def test():
    for x in range(422825,423545):
        for y in range(-711335, -710035):
            getImages([x/1000, y/1000])

#getRoadImages("-35.27801,149.12958", "-35.28032,149.12907")
#getImages(40.457375,-80.009353)
#test()
parseStreetToCoordinates("1383 Boylston St, Boston, MA 02215", "1200 Boylston St, Boston, MA 02215")