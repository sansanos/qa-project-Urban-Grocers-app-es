import sender_stand_request
import data


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
    positive_assert(data.kit_body_one_letter)


# Prueba 2. El número permitido de caracteres (511)
def test_numero_permitido_caracteres_511():
    positive_assert(data.kit_body_511_letters)


# Prueba 3. El número de caracteres es menor que la cantidad permitida (0)
def test_numero_no_permitido_caracteres_0():
    negative_assert(data.kit_body)


# Prueba 4. El número de caracteres es menor que la cantidad permitida (0)
def test_numero_no_permitido_caracteres_512():
    negative_assert(data.kit_body_512_letters)


# Prueba 5. Se permiten caracteres especiales
def test_permite_caracteres_especiales():
    positive_assert(data.kit_body_caracteres_especiales)


# Prueba 6. Se permiten espacios
def test_permite_espacios():
    positive_assert(data.kit_body_espacios)


# Prueba 7. Se permiten números
def test_permite_numeros():
    positive_assert(data.kit_body_numeros)


# Prueba 8. El parámetro no se pasa en la solicitud
def test_no_se_pasa_parametros():
    negative_assert(data.kit_body_sin_parametro)


# Prueba 9. Se ha pasado un tipo de parámetro diferente (número)
def test_parametro_diferente_numero():
    negative_assert(data.kit_body_parametro_diferente)
