from rest_framework import generics
from .models import Billet
from .serializers import BilletSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from .permissions import IsSuperUserPermission
from django.shortcuts import get_list_or_404
import ipdb


class BilletView(generics.ListAPIView):
    queryset: Billet
    serializer_class: BilletSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            billets = Billet.objects.all()
        else:
            billets = Billet.objects.filter(owner=request.user)
        serializer = BilletSerializer(billets, many=True)

        return Response(serializer.data)


class BilletIdView(generics.ListAPIView):
    queryset: Billet
    serializer_class: BilletSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission]

    def get_queryset(self):
        user = self.kwargs["pk"]
        # ipdb.set_trace()
        user = get_list_or_404(Billet, owner=user)
