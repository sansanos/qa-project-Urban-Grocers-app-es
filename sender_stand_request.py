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


