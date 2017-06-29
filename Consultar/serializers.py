from rest_framework import serializers
from Categorias.models import Restaurantes, Esteticas, Hoteles, Veterinarias

class RestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = ('id','name','status','description','horario', 'phone','location','lat','log','img_logo','img_banner','img1','img2','img3','img4','img5')

class EsteticasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esteticas
        fields = ('id','name','status','description','horario', 'phone','location','lat','log','img_logo','img_banner','img1','img2','img3','img4','img5')

class HotelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoteles
        fields = ('id','name','status','description','horario', 'phone','location','lat','log','img_logo','img_banner','img1','img2','img3','img4','img5')

class VeterinariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarias
        fields = ('id','name','status','description','horario', 'phone','location','lat','log','img_logo','img_banner','img1','img2','img3','img4','img5')