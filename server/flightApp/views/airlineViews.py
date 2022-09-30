
from rest_framework.decorators import api_view
from ..models import   Airline_Companies, Countries, Flights
from ..serailizers import  Airline_CompanySerializer, FlightSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from django.contrib.auth.models import User


# permision - Staff Airline Companys Users and Super User
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createFlight(request):
    tempAirline=request.data['airline_company']
    tempOrigin=request.data['origin_country']
    tempDestination=request.data['destination_country']

    airline_company = Airline_Companies.objects.get (id=tempAirline)
    origin_country= Countries.objects.get (id=tempOrigin)
    destination_country = Countries.objects.get (id=tempDestination)

    flight = Flights.objects.create(
            airline_company = airline_company,
            origin_country = origin_country,
            destination_country = destination_country,
            departure_time = request.data['departure_time'],
            landing_time = request.data['landing_time'],
            remaining_tickets = request.data['remaining_tickets']
        )

    serializer = FlightSerializer(flight, many=False)
    return Response(serializer.data)



# permision - Staff Airline Companys Users and Super User
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateFlight(request, id):
    data = request.data
    changing=Flights.objects.get(id = id)

    changing.remaining_tickets = data['remaining_tickets']
    changing.departure_time = data['departure_time']
    changing.landing_time = data['landing_time']
    changing.save()

    serializer = FlightSerializer(changing, many=False)
    return Response(serializer.data)
  


# permision - Staff Airline Companys Users and super user
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteFlight(request,id):
    temp = Flights.objects.get(id=id)
    temp.delete()
    return Response("Flight was deleted") 


# permision - Super user
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addAirCompany(request):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    
    user_id = request.data['user']
    country_id =request.data['country']
    user=User.objects.get(id=user_id)
    country= Countries.objects.get(id=country_id)
    airlineCompany = Airline_Companies.objects.create(
        user = user,
        country = country,
        name = request.data['name']
        )
    serializer = Airline_CompanySerializer(airlineCompany, many=False)
    return Response(serializer.data)  




# permision - Super user
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteAirCompany(request,id):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    temp = Airline_Companies.objects.get(id=id)
    temp.delete()
    return Response("Airline company was deleted")