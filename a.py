# "type": "SELLER",
#     "email": "teste@sandboxpagseguro.com.br",
#     "business_category": "ARCHITECTURAL_AND_ENGINEERING",
#     "person": {
#         "birth_date": "1994-07-03",
#         "name": "TESTE LTDA",
#         "tax_id": "11111111111111",
#         "mother_name": "Maria da Silva",
#         "address": {
#             "region_code": "SP",
#             "city": "São Paulo",
#             "postal_code": "00000000",
#             "street": "Rua São Paulo",
#             "number": "1",
#             "complement": "A",
#             "locality": "Centro",
#             "country": "BRA"
#         },
#         "phones": [
#             {
#                 "area": "11",
#                 "country": "55",
#                 "number": "981111111"
#             }
#         ]
#     },
#     "company": {
#         "name": "Teste LTDA",
#         "tax_id": "00000000000000",
#         "address": {
#             "region_code": "SP",
#             "city": "Sao Paulo",
#             "postal_code": "11111111",
#             "street": "Rua São Paulo",
#             "number": "1",
#             "complement": "A",
#             "locality": "Centro",
#             "country": "BRA"
#         },
#         "phones": [
#             {
#                 "area": "11",
#                 "country": "55",
#                 "number": "911111111"
#             }
#         ]
#     },
#     "tos_acceptance": {
#         "user_ip": "127.0.0.1",
#         "date": "2019-04-17T20:07:07.002-02"
#   }


import requests
import json

url = "{{url}}/accounts"

payload = json.dumps({
  "id": "ACCO_737348328392943",
  "type": "SELLER",
  "created_at": "2019-04-17T20:07:07.002-02",
  "token": {
    "token_type": "bearer",
    "access_token": "2YotnF67589ZFEjr1zCsicMWpAA",
    "expires_in": "36000",
    "refresh_token": "tGzv3JOkF078300XG5Qx2TlKWIA",
    "scope": "accounts.read payments.create"
  },
  "email": "pagseguro@sandboxpagseguro.com.br",
  "business_category": "LEGAL_SERVICE",
  "person": {
    "birth_date": "2004-07-03",
    "name": "Nome completo sem abreviações exatamente como consta no documento",
    "tax_id": "09555683743",
    "mother_name": "Nome completo da mãe sem abreviações exatamente como consta no documento",
    "address": {
      "region_code": "SP",
      "city": "Nome da cidade sem caracteres especiais",
      "postal_code": "65432467",
      "street": "Nome da rua sem caracteres especiais",
      "number": "170",
      "complement": "Bloco do predio",
      "locality": "Nome do bairro sem caracteres especiais",
      "country": "BRA"
    },
    "phones": [
      {
        "area": "11",
        "country": "55",
        "number": "982247672"
      }
    ]
  },
  "company": {
    "name": "Razao Social exatamente como consta no documento",
    "tax_id": "04607332000190",
    "address": {
      "region_code": "SC",
      "city": "Nome da cidade sem caracteres especiais",
      "postal_code": "65432467",
      "street": "Nome da rua sem caracteres especiais",
      "number": "170",
      "complement": "",
      "locality": "Nome do bairro sem caracteres especiais",
      "country": "BRA"
    },
    "phones": [
      {
        "area": "11",
        "country": "55",
        "number": "982247672"
      }
    ]
  },
  "tos_acceptance": {
    "user_ip": "IP VÁLIDO",
    "date": "2019-04-17T20:07:07.002-02"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{token}}',
  'X_CLIENT_ID': '{{client_id}}',
  'X_CLIENT_SECRET': '{{client_secret}}',
  'Accept-Language': 'pt-br'
}

response = requests.request("OBJ", url, headers=headers, data=payload)

print(response.text)