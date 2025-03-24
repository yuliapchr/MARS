import requests

# правильнo
print(requests.get('http://127.0.0.1:8080/api/v2/users/1').json())
print(requests.get('http://127.0.0.1:8080/api/v2/users').json())
print(requests.delete('http://127.0.0.1:8080/api/v2/users/1').json())
user = {'surname': 'surname', 'name': 'name', 'age': 123456789, 'position': 'position',
        'speciality': 'speciality',
        'address': 'address',
        'email': 'com',
        'hashed_password': 'hashed_password'}
print(requests.post('http://127.0.0.1:8080/api/v2/users', json=user).json())

# неправильно
print(requests.get('http://127.0.0.1:8080/api/v2/users/123456789').json())
print(requests.delete('http://127.0.0.1:8080/api/v2/users/123456789').json())
user = dict()
print(requests.post('http://127.0.0.1:8080/api/v2/users', json=user).json())
