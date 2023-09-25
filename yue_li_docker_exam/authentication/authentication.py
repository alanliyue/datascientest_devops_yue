import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_backend'
# port de l'API
api_port = 8000

list_users = ['alice', 'bob', 'clementine']
list_passwords = ['wonderland', 'builder', 'mandarine']
user_password_db = zip(list_users, list_passwords)


# requête
for user_password in user_password_db: 
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params= {
            'username': user_password[0],
            'password': user_password[1]
        }
    )

    output = '''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username={username}
    | password={password}

    expected result = 200
    actual restult = {status_code}

    ==>  {test_status}

    '''


    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    test_log = output.format(username=user_password[0], password=user_password[1], status_code=status_code, test_status=test_status)
    print(test_log)
    # impression dans un fichier
    if os.environ.get('LOG') == "1":
        print("writing to the log")
        with open('/home/yue_li/logs/api_test.log', 'a') as file:
            file.write(test_log)
