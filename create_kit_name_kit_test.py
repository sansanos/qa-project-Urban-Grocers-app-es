import sender_stand_request
import data


def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = name
    return current_kit_body


# Función de prueba positiva
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body['name']


# Función de prueba negativa
def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


# Prueba 1. En el parámetro name el número permitido de caracteres (1)
def test_numero_permitido_caracteres_1():
    kit_body = get_kit_body(data.kit_body_one_letter)
    positive_assert(kit_body)


# Prueba 2. El número permitido de caracteres (511)
def test_numero_permitido_caracteres_511():
    kit_body = get_kit_body(data.kit_body_511_letters)
    positive_assert(kit_body)


# Prueba 3. El número de caracteres es menor que la cantidad permitida (0)
def test_numero_no_permitido_caracteres_0():
    kit_body = get_kit_body(data.kit_body_no_letter)
    negative_assert(kit_body)


# Prueba 4. El número de caracteres es menor que la cantidad permitida (0)
def test_numero_no_permitido_caracteres_512():
    kit_body = get_kit_body(data.kit_body_512_letters)
    negative_assert(kit_body)


# Prueba 5. Se permiten caracteres especiales
def test_permite_caracteres_especiales():
    kit_body = get_kit_body(data.kit_body_caracteres_especiales)
    positive_assert(kit_body)


# Prueba 6. Se permiten espacios
def test_permite_espacios():
    kit_body = get_kit_body(data.kit_body_espacios)
    positive_assert(kit_body)


# Prueba 7. Se permiten números
def test_permite_numeros():
    kit_body = get_kit_body(data.kit_body_numeros)
    positive_assert(kit_body)


# Prueba 8. El parámetro no se pasa en la solicitud
def test_no_se_pasa_parametros():
    kit_body = get_kit_body(data.kit_body_sin_parametro)
    negative_assert(kit_body)


# Prueba 9. Se ha pasado un tipo de parámetro diferente (número)
def test_parametro_diferente_numero():
    kit_body = get_kit_body(data.kit_body_parametro_diferente)
    negative_assert(kit_body)
