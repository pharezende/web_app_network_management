import urllib.request
import json

ALL_post = True
ALL_get = False
ALL_delete = False

Single_post = False
Single_get = True
Single_delete = False


print("#####ALL#####")

#All
address_all = "http://127.0.0.1:5000/hosts/all/"

#POST
if ALL_post:
    body_post = [
        {
            "name": "H1",
            "numberOfInterfaces": 1
        },
        {
            "name": "H2",
            "numberOfInterfaces": 3
        },
        {
            "name": "H3",
            "numberOfInterfaces": 2
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


#Single
address_single = "http://127.0.0.1:5000/hosts/single/"


print("#####SINGLE#####")

#POST
if Single_post:
    body_post = {
        "name": "H5",
        "numberOfInterfaces": 1,
    }
    req = urllib.request.Request(address_single)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_post)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)

#GET
if Single_get:
    address_single = "http://127.0.0.1:5000/hosts/single/H2"

    req = urllib.request.Request(address_single, method='GET')
    response = urllib.request.urlopen(req)
    print(json.loads(response.read()))

#DELETE
if Single_delete:
    body_delete = {
        "name": "H5"
    }

    req = urllib.request.Request(address_single, method='DELETE')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_delete)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
