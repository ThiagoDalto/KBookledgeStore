from rest_framework import generics
from .models import Paymount
from .serializers import PaymountsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from .permissions import IsSuperUserPermission
import ipdb


class PaymountsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Paymount.objects.all()
    serializer_class = PaymountsSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            paymounts = Paymount.objects.all()
        else:
            paymounts = Paymount.objects.filter(reference_id=request.user)
        serializer = PaymountsSerializer(paymounts, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):

        serializer.save(reference=self.request.user, data=self.request.data)


class PaymountsIdView(generics.ListAPIView):
    queryset = Paymount.objects.all()
    serializer_class = PaymountsSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission]

    def get(self, request, *args, **kwargs):
        pass
