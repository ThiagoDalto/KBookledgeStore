from .models import Promotions
from .serializers import PromotionsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class PromotionView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    
    queryset = Promotions.objects.all()

    serializer_class = PromotionsSerializer

class PromotionDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Promotions.objects.all()

    serializer_class = PromotionsSerializer

# primeiro fazer o serializer para usar as views
# depois fazer as views
# por último as URL
# pode seguir o exemplo de users
# quando for criar a tabela promoção fazer relação com books pelo ID, o user não faz isso
