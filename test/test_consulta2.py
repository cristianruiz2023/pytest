import pytest
import requests
import os


person_number = os.environ.get('ID_test')
def test_get():
    #consuming the api
    answer_get = requests.get(f'http://cursotesting.com.ar:3000/consultapersona/{person_number}')
    #protocol + url + port number + parameters 
    print(answer_get)
    response_received = answer_get.json()
    #casting response to json
    print(response_received)
    assert response_received['nombre'] == 'Enzo2'
    assert response_received['apellido'] == 'Ruiz2'

if __name__ == '__main__':
    pytest.main(['-s',__file__])

# -s muestra en los resultados los prints de las lineas 8 y 10 en el detalle del test
#-s show in the results the prints of lines 8 and 10