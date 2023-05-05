from billets.models import Billet
from datetime import datetime, timedelta

import requests
import json
import ast
import ipdb


class BilletMethod():
    def billet(validated_data, url, user, address, orders):
        # url = "https://sandbox.api.pagseguro.com/charges"

        # orders = Order.objects.filter(user=validated_data["reference"])
        # address = get_object_or_404(Address, pk=validated_data["reference"].address_id)
        # user = get_object_or_404(User, pk=validated_data["reference"].id)

        payload = json.dumps(
            {
                "reference_id": str(validated_data["reference"].id),
                # "description": validated_data["description"],
                "amount": {
                    "value": int(sum([order.on_price for order in orders]) * 100),
                    "currency": "BRL",
                },
                "payment_method": {
                    "type": "BOLETO",
                    "boleto": {
                        "due_date": (datetime.now() + timedelta(days=3)).strftime(
                            "%Y-%m-%d"
                        ),
                        "instruction_lines": {
                            "line_1": "Pagamento processado para DESC Fatura",
                            "line_2": "Via PagSeguro",
                        },
                        "holder": {
                            "name": validated_data["reference"].username,
                            "tax_id": "22222222222",
                            "email": validated_data["reference"].email,
                            "address": {
                                "street": address.street_address,
                                "number": address.number,
                                "locality": address.neighborhood,
                                "city": address.city,
                                "region": address.state,  # opcional
                                "region_code": "SP",
                                "country": address.country,
                                "postal_code": address.zip_code,
                            },
                        },
                    },
                },
                # "notification_urls": [
                #     "https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-4c3f4a1fdc46/"
                # ]
            }
        )
        headers = {
            "Authorization": "afc90184-87f6-41c0-9a58-f15403a5d466b365f70c4196bbf5f7974c1c637d20f1cf22-08f6-4e18-849d-c5090514ff7c",
            "Content-Type": "application/json",
            "x-api-version": "4.0",
            "x-idempotency-key": "",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        paymount_data = ast.literal_eval(response.text)

        validated_data.pop("data")
        validated_data["reference"] = user
        validated_data["status"] = paymount_data["status"]
        validated_data["value"] = paymount_data["amount"]["value"]
        validated_data["payment_method"] = paymount_data["payment_method"]["type"]
        validated_data["description"] = paymount_data["description"]
        validated_data["created_at"] = paymount_data["created_at"]
        validated_data["link_billet_pdf"] = paymount_data["links"][0]["href"]
        validated_data["link_billet_png"] = paymount_data["links"][1]["href"]

        # building billet arguments
        billet_data = {
            "owner": user,
            "barcode": paymount_data["payment_method"]["boleto"]["barcode"],
            "value": paymount_data["amount"]["value"],
            "formatted_barcode": paymount_data["payment_method"]["boleto"]["formatted_barcode"],
            "due_date": paymount_data["payment_method"]["boleto"]["due_date"],
            "link_pdf": paymount_data["links"][0]["href"],
            "link_png": paymount_data["links"][1]["href"]
        }
        billet = Billet.objects.create(**billet_data)
        validated_data["billet"] = billet

        return validated_data
