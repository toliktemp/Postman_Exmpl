from utilities.configurations import *


def add_new_student(firstName, lastName, middleName, dob):
    body = {
        "first_name": firstName,
        "last_name": lastName,
        "middle_name": middleName,
        "date_of_birth": dob
    }
    return body


def update_student_info(stud_id, firstName, lastName, middleName, dob):
    body = {
        "id": stud_id,
        "first_name": firstName,
        "last_name": lastName,
        "middle_name": middleName,
        "date_of_birth": dob
    }
    return body
