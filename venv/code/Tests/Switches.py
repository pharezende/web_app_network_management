import urllib.request
import json

ALL_post = False
ALL_get = False
ALL_delete = False

Single_post = False
Single_get = False
Single_delete = True

print("#####ALL#####")

#All
address_all = "http://127.0.0.1:5000/switches/all/"

#POST
if ALL_post:
    body_post = [
        {
            "name": "S1",
            "numberOfInterfaces": 48,
            "manufacturer": "Cisco"
        },
        {
            "name": "S2",
            "numberOfInterfaces": 24,
            "manufacturer": "Juniper"
        }
    ]

    req = urllib.request.Request(address_all)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_post)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)

#GET
if ALL_get:
    req = urllib.request.Request(address_all, method='GET')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    response = urllib.request.urlopen(req)
    print(json.loads(response.read()))

#DELETE
if ALL_delete:
    req = urllib.request.Request(address_all, method='DELETE')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    response = urllib.request.urlopen(req)
    print(json.loads(response.read()))

#Single
address_single = "http://127.0.0.1:5000/switches/single/"


print("#####SINGLE#####")

#POST
if Single_post:
    body_post = {
        "name": "S3",
        "numberOfInterfaces": 48,
        "manufacturer": "Cisco"
    }
    req = urllib.request.Request(address_single)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_post)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)

#GET
if Single_get:

    body_get = {
        "name": "S2"
    }

    req = urllib.request.Request(address_single, method='GET')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_get)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    print(json.loads(response.read()))

#DELETE
if Single_delete:
    body_delete = {
        "name": "S1"
    }

    req = urllib.request.Request(address_single, method='DELETE')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_delete)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)

