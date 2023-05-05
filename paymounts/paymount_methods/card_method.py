from billets.models import Billet
from datetime import datetime, timedelta

import requests
import json
import ast
import ipdb


class CardMethod:
    def card(validated_data, url, user, orders):

        payload = json.dumps(
            {
                "reference_id": str(validated_data["reference"].id),
                # "description": validated_data["description"],
                "amount": {
                    "value": int(sum([order.on_price for order in orders]) * 100),
                    "currency": "BRL",
                },
                "payment_method": {
                    "type": validated_data["data"]["payment_method"],
                    "installments": 1,  # prestações/parcelas
                    "capture": True,
                    "soft_descriptor": "Book Ledge Store",
                    "card": {
                        "number": validated_data["data"]["number"],
                        "exp_month": validated_data["data"]["exp_month"],
                        "exp_year": validated_data["data"]["exp_year"],
                        "security_code": validated_data["data"]["security_code"],
                        "holder": {"name": user.username},
                    },
                    "authentication_method": {
                        "type": "THREEDS",
                        "cavv": "BwABBylVaQAAAAFwllVpAAAAAAA=",
                        "xid": "BwABBylVaQAAAAFwllVpAAAAAAA=",
                        "eci": "05",
                        "version": "2.1.0",
                        "dstrans_id": "DIR_SERVER_TID",
                    },
                },
                # "notification_urls": [
                #     "https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-4c3f4a1fdc46/"
                # ],
                "metadata": {
                    "Exemplo": "Aceita qualquer informação",
                    "NotaFiscal": "123",
                    "idComprador": str(validated_data["reference"].id),
                },
            }
        )
        headers = {
            "Authorization": "afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c",
            "Content-Type": "application/json",
            "x-api-version": "4.0",
            "x-idempotency-key": "",
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        e = response.text
        paymount_data = json.loads(response.text)

        for order in orders:
            order.status = 3
            order.save()

        validated_data.pop("data")
        validated_data["reference"] = user
        validated_data["status"] = paymount_data["status"]
        validated_data["value"] = paymount_data["amount"]["value"]
        validated_data["payment_method"] = paymount_data["payment_method"]["type"]
        validated_data["description"] = paymount_data["description"]
        validated_data["created_at"] = paymount_data["created_at"]
        validated_data["paid_at"] = paymount_data["paid_at"]
        validated_data["card"] = "***" + paymount_data["payment_method"]["card"]["last_digits"]

        return validated_data
