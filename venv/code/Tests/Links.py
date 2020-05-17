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
address_all = "http://127.0.0.1:5000/links/all/"

#POST
if ALL_post:
    body_post = [
      {
        "src": {
          "name": "R1",
          "interface": 2,
          "ip_address": "10.0.0.1",
          "mask": 24
        },

        "dst": {
          "name": "H1",
          "interface": 1,
          "ip_address": "10.0.0.2",
          "mask": 24
        },

        "bandwidth": "100 Mbps"
      },
        {
            "src": {
                "name": "R2",
                "interface": 1,
                "ip_address": "10.0.0.1",
                "mask": 24
            },

            "dst": {
                "name": "H1",
                "interface": 1,
                "ip_address": "10.0.0.2",
                "mask": 24
            },

            "bandwidth": "100 Mbps"
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
address_single = "http://127.0.0.1:5000/links/single/"


print("#####SINGLE#####")

#POST
if Single_post:
    body_post = {
        "src": {
          "name": "R5",
          "interface": 2,
          "ip_address": "10.0.0.1",
          "mask": 24
        },

        "dst": {
          "name": "H3",
          "interface": 1,
          "ip_address": "10.0.0.2",
          "mask": 24
        },

        "bandwidth": "100 Mbps"
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
        "src": "R2",
        "dst": "H1"
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
        "src": "R1",
        "dst": "H1"
    }

    req = urllib.request.Request(address_single, method='DELETE')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body_delete)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
