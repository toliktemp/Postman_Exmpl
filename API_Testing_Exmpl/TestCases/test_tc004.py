import json
import requests
from utilities.configurations import *
from utilities.payload import *

'''
Verification flow on adding/deleting student
'''


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
    print(json_response)

    print("\n***** Validating Response *****\n")
    print(json_response['status'])
    assert json_response['status'] == 'true'
    print(json_response['data']['first_name'])
    assert json_response['data']['first_name'] == 'John'
    assert json_response['data']['middle_name'] == 'T'
    assert json_response['data']['last_name'] == 'Smith'
    assert json_response['data']['date_of_birth'] == '11/11/1990'


def test_delete_student():

    # url = getConfig()['API']['endpoint']+'api/studentsDetails/3856127'
    url = getConfig()['API']['endpoint']+'api/studentsDetails/'+str(student_id)

    response = requests.delete(url)
    json_response = response.json()

    print(f"\nJson Response: {json_response}\n")
    print("****")
    print(f"Status: {json_response['status']}")
    print(f"MSG: {json_response['msg']}")
    assert json_response['status'] == 'true'
    assert json_response['msg'] == 'Delete  data success'


def test_verify_deleted_student():

    # url = getConfig()['API']['endpoint']+'api/studentsDetails/3856127'
    url = getConfig()['API']['endpoint']+'api/studentsDetails/'+str(student_id)
    response = requests.get(url)
    json_response = response.json()
    print(json_response)

    print("\n***** Verifying - Student Data Deleted *****\n")
    print(response.text)
    print(json_response['status'])
    print(f"MSG: {json_response['msg']}")
    assert json_response['status'] == 'false'
    assert json_response['msg'] == 'No data Found'
