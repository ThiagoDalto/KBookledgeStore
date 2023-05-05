from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Address
from .serializers import AddressSerializer
from users.models import User
from .permissions import Isowner_or_superuser
import requests
from rest_framework.permissions import IsAuthenticated


class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, Isowner_or_superuser]
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):

        if "zip_code" not in request.data or "country" not in request.data or "state" not in request.data:
            return Response(
                {"message": "Data not found"},
                status.HTTP_400_BAD_REQUEST,
            )
        else:
            address_cep = request.data["zip_code"]
            cep = address_cep.replace("-", "").replace(".", "").replace(" ", "")
            try:
                req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            except requests.ConnectionError:
                return Response(status.HTTP_400_BAD_REQUEST)

            dict_address = req.json()

            dict_address["city"] = dict_address.get("localidade", "")
            dict_address["neighborhood"] = dict_address.get("bairro", "")
            dict_address["uf"] = dict_address.get("uf", "")
            dict_address["street_address"] = dict_address.get("logradouro", "")
            dict_address["complement"] = dict_address.get("complemento", "")
            request.data.update({**dict_address})

            return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = User.objects.get(pk=self.request.user.id)
        serializer.save()
        address_id = serializer.data.get("id")

        address = Address.objects.get(pk=address_id)

        user.address = address
        user.save()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Address.objects.all()
        return Address.objects.filter(user=self.request.user)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, Isowner_or_superuser]
    serializer_class = AddressSerializer

    queryset = Address.objects.all()
