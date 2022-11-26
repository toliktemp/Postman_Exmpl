import json
import requests
import configparser
from utilities.configurations import *
from utilities.payload import *


def test_add_new_student():

    global student_id

    url = getConfig()['API']['endpoint']+'api/studentsDetails'
    new_student_info = add_new_student('John', 'Smith', 'T', '11/11/1990')

    response = requests.post(url, json=new_student_info,)
    json_response = response.json()

    print("\n***** Response Content ***** \n")
    # print(response.text)
    print(response.json())

    print(f"\nResponse Status Code: {response.status_code}")
    assert response.status_code == 201

    print(f"\nStudent ID: {json_response['id']}")
    student_id = json_response['id']

    print(type(student_id))
    student_id = json_response['id']


def test_get_student_details():
    url = getConfig()['API']['endpoint']+'api/studentsDetails/'+str(student_id)

    response = requests.get(url)
    json_response = response.json()
    # print(response.text)
    # print(response.json())
    print(response.content)
    print("\n ***\n")
    print(json_response)

    print("\n***** Verifying - Student Data  *****\n")
    print(f"Status is : {json_response['status']}")
    assert json_response['status'] == 'true'

    print(json_response['data']['first_name'])
    assert json_response['data']['first_name'] == 'John'

    print(json_response['data']['last_name'])
    assert json_response['data']['last_name'] == 'Smith'

    print(json_response['data']['middle_name'])
    assert json_response['data']['middle_name'] == 'T'

    print(json_response['data']['date_of_birth'])
    assert json_response['data']['date_of_birth'] == '11/11/1990'
