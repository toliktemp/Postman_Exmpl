import requests

'''
# http://rahulshettyacademy.com
# 'visit-month'

Send and Manage Cookies through API request
Redirection and Time out
Send Attachments through API calls (post multiple multipart- encoded files)

'''


def test_redirects():

    cookie = {'visit-month': 'February'}
    response = requests.get('http://rahulshettyacademy.com',
                            allow_redirects=False,
                            cookies=cookie, timeout=1)

    # Redirection to => 301, and then used actual URL after200

    print(f"\n\n Response History: {response.history}")
    print("\n ***** \n")
    print(response.status_code)


def test_cookies():

    se = requests.session()
    se.cookies.update({'visit-month': 'February'})

    response = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})

    print("\n ***** Response ***** \n")
    print(response.text)


def test_post_encoded_files():

    url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
    files = {'file': open('/Users/tolik/PycharmProjects/Project_API_Example/TestCases/image.png', 'rb')}
    response = requests.post(url, files=files)
    print(f"\nStatus Code: {response.status_code}")
    # print(response.text)
    print(response.json())
    print(response.json()['message'])
