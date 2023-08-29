import pytest
import requests
import os

def test_create_new_person():
    api_new = 'http://cursotesting.com.ar:3000/nuevapersona/'
    data = {
        'nombre': 'Enzo',
        'apellido': 'Ruiz',
        'edad': '7'

    }
    #consumiendo la api
    answer_post = requests.post(api_new, json=data)
    print(answer_post)
    
    response_received = answer_post.json()
    #casting response to json
    print(response_received)
    assert answer_post.status_code == 200, f'devolvio el codigo {answer_post.status_code}'
    assert 'id' in response_received, 'error no devolvio id'

    if answer_post.status_code == 200:
        print('everything worked ok')
        os.environ['ID_test'] = str(response_received['id'])
        assert response_received['id'] > 10000
    else:
        print('The server does not respond')
        #assert response_received == 'success'

if __name__ == '__main__':
    pytest.main(['-s',__file__])
