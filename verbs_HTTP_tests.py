import requests
import os
from dotenv import load_dotenv
from jsonschema import validate

load_dotenv()

MY_URL = os.getenv('URL')

def test_get_users():

    response = requests.get(MY_URL)

    SCHEMA_VALIDATE_GET = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "name": {
        "type": "string"
      },
      "username": {
        "type": "string"
      },
      "email": {
        "type": "string"
      },
      "address": {
        "type": "object",
        "properties": {
          "street": {
            "type": "string"
          },
          "suite": {
            "type": "string"
          },
          "city": {
            "type": "string"
          },
          "zipcode": {
            "type": "string"
          },
          "geo": {
            "type": "object",
            "properties": {
              "lat": {
                "type": "string"
              },
              "lng": {
                "type": "string"
              }
            },
            "required": [
              "lat",
              "lng"
            ]
          }
        },
        "required": [
          "street",
          "suite",
          "city",
          "zipcode",
          "geo"
        ]
      },
      "phone": {
        "type": "string"
      },
      "website": {
        "type": "string"
      },
      "company": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "catchPhrase": {
            "type": "string"
          },
          "bs": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "catchPhrase",
          "bs"
        ]
      }
    },
    "required": [
      "id",
      "name",
      "username",
      "email",
      "address",
      "phone",
      "website",
      "company"
    ]
  }
}
    
    assert response.status_code == 200
    assert (validate(response.json(), SCHEMA_VALIDATE_GET)) == None

def test_post_users():
    MY_USER_DATA = {
        'name': 'Lucilene Bruneli',
        'username': 'lu.bruneli',
        'email': 'lu.bruneli@hotmail.com',
        'address': {
        'street': 'Rua Vazia',
        'suite': 'Suite 000',
        'city': 'São Bernardo',
        'zipcode': '28510-250',
        'geo': {
            'lat': '-34.2406',
            'lng': '54.2031'
        }
        },
        'phone': '884-718-3254',
        'website': 'bruneli.net',
        'company': {
        'name': 'Bruneli QA LTDA',
        'catchPhrase': 'Deliver with quality and precision',
        'bs': 'backend frontend models'
        }
    }

    response = requests.post(MY_URL, MY_USER_DATA)

    SCHEMA_VALIDATE_POST = {
        "type": "object",
        "properties": {
            "id": {
            "type": "integer"
            }
        },
        "required": [
            "id"
        ]
    }

    assert response.status_code == 201
    assert (validate(response.json(), SCHEMA_VALIDATE_POST)) == None

def test_put_users():
    MY_ID = 9
    MY_NEW_DATA = {
        'phone': '554-719-3004',
        'website': 'bruneli.var',
        'company': {
            'name': 'Bruneli QA',
            'catchPhrase': 'Always getting better with quality',
            'bs': 'backend frontend e2e models'
        }
    }
    CONCAT_URL = MY_URL + '/' + str(MY_ID)

    response = requests.put(CONCAT_URL, MY_NEW_DATA)

    SCHEMA_VALIDATE_PUT = {
        "type": "object",
        "properties": {
            "phone": {
            "type": "string"
            },
            "website": {
            "type": "string"
            },
            "company": {
                "properties": {
                    "name": {
                    "type": "string"
                    },
                    "catchPhrase": {
                    "type": "string"
                    },
                    "bs": {
                    "type": "string"
                    }
            },
            "required": [
                "name",
                "catchPhrase",
                "bs"
            ]
            },
            "id": {
            "type": "integer"
            }
        },
        "required": [
            "phone",
            "website",
            "company",
            "id"
        ]
    }

    assert response.status_code == 200
    assert (validate(response.json(), SCHEMA_VALIDATE_PUT)) == None

def test_delete_users():
    MY_ID = 8
    CONCAT_URL = MY_URL + '/' + str(MY_ID)

    response = requests.delete(CONCAT_URL)

    SCHEMA_VALIDATE_DEL = {
        "type": "object"
    }

    assert response.status_code == 200
    assert (validate(response.json(), SCHEMA_VALIDATE_DEL)) == None