from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def teste_html_deve_retornar_ok_e_olamundo(client):
    response = client.get('/helloworld')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá mundo, bão?</h1>' in response.text


def teste_post_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'joao',
            'email': 'joar@email.com',
            'password': 'segredo',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'joao',
        'email': 'joar@email.com',
        'id': 1,
    }


def teste_get_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'joao', 'email': 'joar@email.com', 'id': 1}]
    }


def teste_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'carlos',
            'email': 'carlos@email.com',
            'password': 'senhasegura',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'carlos',
        'email': 'carlos@email.com',
        'id': 1,
    }


def teste_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
