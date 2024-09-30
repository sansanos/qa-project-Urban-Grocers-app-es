import configuration
import requests
import data

def user_token():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH)

response = get_user_token()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

authToken = post_new_user(user_body).json()['authToken']

header_kit = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {authToken}'
}

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_new_kit(new_kit):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, # Concatenación de URL base y ruta.
                         json=new_kit, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


response = post_new_kit(data.new_kit);
print(response.status_code)
print(response.json())