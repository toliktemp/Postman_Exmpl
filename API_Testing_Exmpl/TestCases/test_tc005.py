import json
import requests
import configparser
from utilities.configurations import *

'''
Verification: Headers, validating some students data, elapsed time
'''

def test_get_all_students_list():
    # url = "https://thetestingworldapi.com/api/studentsDetails"
    url = getConfig()['API']['endpoint']+'api/studentsDetails'

    response = requests.get(url)
    json_response = response.json()

    print(f"json_response type: {type(json_response)}")     # class list

    print("\n***** Response Status Code *****")
    print(f"Response Status Code: {response.status_code}")

    print("\n***** For Easy Viewing Readable Response *****")
    data = json.dumps(json_response, indent=2, sort_keys=True)
    print(type(data))                           # type string

    print(f"Length : {len(data)}")
    # print(data)

    print("\n***** Response Headers *****\n")
    print(f"Type of response headers: {type(response.headers)}")        # Dictionary
    print(response.headers)

    print("\n***** All Headers key => value pairs *****\n")
    for k, v in response.headers.items():
        print(f"{k} =>  {v}")

    print("\n***** Get total items in headers *****\n")
    print(f"Total Headers: {len(response.headers)} ")
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.headers['Server'] == 'Microsoft-IIS/8.5'
    assert response.headers['X-AspNet-Version'] == '4.0.30319'

    print("\n***** Fetching Student Details  *****\n")
    print("\nFirst Student")
    print(f"ID: {json_response[0]['id']}")
    print(f"First Name: {json_response[0]['first_name']}")
    print(f"Last Name: {json_response[0]['last_name']}")
    print(f"Date of Birth: {json_response[0]['date_of_birth']}")

    print("\nLast Student")
    print(f"ID: {json_response[99]['id']}")
    print(f"First Name: {json_response[99]['first_name']}")
    print(f"Last Name: {json_response[99]['last_name']}")
    print(f"Date of Birth: {json_response[99]['date_of_birth']}")

    print("\n***** Encoding *****\n")
    print(response.encoding)

    print("***** Cookies *****")
    print(response.cookies)

    print("\n***** Elapsed Time *****\n")
    print(response.elapsed)



