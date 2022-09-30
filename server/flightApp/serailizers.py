
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Order,Countries,Airline_Companies,Tickets,Flights

class UserSerializer(serializers.ModelSerializer):
    name= serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isSuperUser = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User 
        fields = ['id','_id','username','email','name','isAdmin','isSuperUser']

    def get__id(self,obj):
        return obj.id

    def get_isAdmin(self,obj):
        return obj.is_staff

    def get_isSuperUser(self,obj):
        return obj.is_superuser

    def get_name(self,obj):
        name = obj.first_name
        if name=="":
            name = obj.email
        return name

        
class UserSerializerWithToken(UserSerializer):
    token= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model =User
        fields = ['id','_id','username','email','name','isAdmin','token','isSuperUser']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)
    # tickets = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields ='__all__'

    def get_User(self,obj):
        order = obj.user
        serializer = UserSerializer(order,many=False)
        return serializer.data

    def getTicket(self,obj):
        ticket = obj.ticket_set.all()
        serializer = TicketsSerializer(ticket,many=True)
        return serializer.data


class CountrySerializer(serializers.ModelSerializer):
    # airline_company = serializers.SerializerMethodField(read_only=True)
    # flights = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Countries
        fields ='__all__'

    def get__id(self,obj):
        return obj.id
    
    def get_airline(self,obj):
        items = obj.airline_set.all()
        serializer =Airline_CompanySerializer(items,many=True)
        return serializer.data

    def get_flights(self,obj):
        items = obj.flights_set.all()
        serializer = FlightSerializer(items,many=True)
        return serializer.data


class Airline_CompanySerializer(serializers.ModelSerializer):
    # flights = serializers.SerializerMethodField(read_only=True)
    # User = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Airline_Companies
        fields ='__all__'  

    def get__id(self,obj):
        return obj.id  

    def get_flights(self,obj):
        items = obj.flights_set.all()
        serializer = FlightSerializer(items,many=True)
        return serializer.data  

    def get_User(self,obj):
        items = obj.user
        serializer = UserSerializer(items,many=False)
        return serializer.data

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields ='__all__'  
                     

class FlightSerializer(serializers.ModelSerializer):
    # tickets = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Flights
        fields ='__all__' 

    def get__id(self,obj):
        return obj.id
        
    def getTicket(self,obj):
        ticket = obj.ticket_set.all()
        serializer = TicketsSerializer(ticket,many=True)
        return serializer.data  
                 
