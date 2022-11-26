import requests

'''
Adding customized headers into get request and header verification
'''


def test_customized_headers():
    # Customized header
    header_data = {
        "New-Server": "Microsoft-IIS/8.5",
        "Cache-Control": "no-cache",
        "X-AspNet-Version": "4.0.30319"
    }

    # Customized params
    param = {'name': 'testingworld', 'email': 'testingworld@example.com', 'phone': '+380-482-652310'}

    response = requests.get('http://httpbin.org/get', headers=header_data, params=param)

    # print(f"type response text: {type(response.text)}")     # str
    # print(f"type response header: {type(response.headers)}")    # dict

    print("\n\n ********** \n")

    print(response.text)

    print("\n\n ********** \n")
    print(response.headers)

    print(f"Total Headers: {len(response.headers)} ")

    print("\n***** All Headers key => value pairs *****\n")
    for k, v in response.headers.items():
        print(f"{k} =>  {v}")

    print(response.headers['Content-Length'])
    # assert response.headers['Content-Length'] == '419'

    print(response.headers['Access-Control-Allow-Credentials'])
    assert response.headers['Access-Control-Allow-Credentials'] == 'true'

    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application/json'

    print("\n***** Elapsed Time *****\n")
    print(response.elapsed)
