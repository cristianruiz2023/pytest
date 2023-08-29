import os
import pytest
import requests

#api recibe datos en espanol
def test_put():
    person_number = os.environ.get('ID_test')
    api_modify = f'http://cursotesting.com.ar:3000/cambiar/{person_number}'
    data = {
        'nombre': 'Enzo2',
        'apellido': 'Ruiz2'

    }
    #consumiendo la api
    answer_put = requests.put(api_modify, json=data)
    #codigo de respuesta
    print(answer_put)
  
if __name__ == '__main__':
    pytest.main(['-s',__file__])
