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
    headers = data.headers.copy()
    token = auth_token_return
    headers["Authorization"] = f"Bearer {token}"

    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             headers=headers,
                             json=kit_body)

    return response


