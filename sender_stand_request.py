import configuration
import requests
import data


def create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers.copy)


def auth_token_return():
    response = create_new_user(data.body.copy())
    token = response.json['authToken']
    return token


def post_new_client_kit(kit_body):
    token = auth_token_return
    authorization = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=authorization,
                         json=kit_body)


''''
def get_new_user_token():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body.copy())


response = get_new_user_token()
print(response.status_code)
print(response.json())


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body.copy(),
                         headers=data.headers.copy())


authToken = post_new_user(data.user_body).json()["authToken"]
response = post_new_user(data.user_body)

authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {authToken}'
}

print(response.status_code)
print(response.json())


def post_new_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.kit_body.copy(),
                         headers=authorization)


response = post_new_kit(data.kit_body)

authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {authToken}'
}

print(response.status_code)
print(response.json())
'''
