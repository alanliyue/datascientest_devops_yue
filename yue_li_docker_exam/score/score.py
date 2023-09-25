import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_backend'
# port de l'API
api_port = 8000

username = 'alice'
password = 'wonderland'
versions = ['v1', 'v2']
# requête
for version in versions: 
    r = requests.get(
        url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
        params= {
            'username': username,
            'password': password,
            'sentence': 'life is beautiful'
        }
    )

    output = '''
    ============================
        Score test {version}
    ============================

    request done at "/{version}/sentiment"
    | username={username}
    | password={password}
    | sentence='life is beautiful'

    expected result > 0
    actual restult = {score}

    ==>  {test_status}

    '''


    # réponse de la requête
    score = r.json().get('score')

    # affichage des résultats
    if score > 0:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    test_log = output.format(username=username, password=password, score=score, test_status=test_status, version=version)
    print(test_log)
    # impression dans un fichier
    if os.environ.get('LOG') == "1":
        print("writing to the log")
        with open('/home/yue_li/logs/api_test.log', 'a') as file:
            file.write(test_log)

    r = requests.get(
        url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
        params= {
            'username': username,
            'password': password,
            'sentence': 'that sucks'
        }
    )

    output = '''
    ============================
        Score test {version}
    ============================

    request done at "/{version}/sentiment"
    | username={username}
    | password={password}
    | sentence='that sucks'

    expected result < 0
    actual restult = {score}

    ==>  {test_status}

    '''


    # réponse de la requête
    score = r.json().get('score')

    # affichage des résultats
    if score < 0:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    test_log = output.format(username=username, password=password, score=score, test_status=test_status, version=version)
    print(test_log)
    # impression dans un fichier
    if os.environ.get('LOG') == "1":
        print("writing to the log")
        with open('/home/yue_li/logs/api_test.log', 'a') as file:
            file.write(test_log)
