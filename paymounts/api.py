import requests
import json
import ipdb

token_prod = "17a8c0a2-70aa-456a-a480-63e5ecb7e220f1309f1d4cdebec08e738a617027e0f7e85c-2875-4da6-905c-369650a68d71"


#                    Criando aplicação para poder criar ações em nome do usuário
def createAppication():
    url_test = "https://sandbox.api.pagseguro.com/oauth2/application"
    # url_prod = "https://api.pagseguro.com/oauth2/application"

    payload = json.dumps({
        "name": "KBookLedgeStore",
        "description": "É uma plataforma de venda de EBooks",
        "site": "https://web-production-544c.up.railway.app/api/",
        "redirect_uri": "https://web-production-544c.up.railway.app/api/",
        # "logo": "https://web-production-544c.up.railway.app/api/media/book_adobe_express.svg"
    })
    headers = {
        'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url_test, headers=headers, data=payload)

    print(response.text)


# createAppication()
# ________________________________________________________________________________________
# RESPONSE -> {
#   "name":"KBookLedgeStore",
#   "description":"É uma plataforma de venda de EBooks",
#   "client_id":"22a9d249-c95f-477a-b164-7cae57c46f72",
#   "client_secret":"f972b704-28d5-439d-816f-0d00cf777222",
#   "site":"https://web-production-544c.up.railway.app/api/",
#   "redirect_uri":"https://web-production-544c.up.railway.app/api/",
#   "account_id":"ACCO_95F26B16-21AC-4B22-952A-7A73FC88BE3E",
#   "client_type":"confidential"
# }
# ________________________________________________________________________________________


def listApplication():
    url = "https://sandbox.api.pagseguro.com/oauth2/application/62d9a6b9-4c61-43c3-b13c-f1519029c1a5"

    payload = {}
    headers = {
        'Authorization': 'Bearer EE0479C3F7B24E3CAC530B2CF074BA25',
        'Content-Type': 'application/json',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


listApplication()
