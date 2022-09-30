
from rest_framework.decorators import api_view
from ..models import  Countries,Flights,Airline_Companies
from ..serailizers import   CountrySerializer, FlightSerializer, Airline_CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getAllCountries(request):
    countries = Countries.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data) 

@api_view(['GET']) 
def getCountry(request,id):
    country = Countries.objects.get(id=id)
    serializer = CountrySerializer(country,many = False)
    return Response(serializer.data) 


@api_view(['GET'])
def getFlight(request, id):
    flight = Flights.objects.get(id=id)
    flight1= ({
            "ID":flight.id,
            "airline": flight.airline_company.name,
            "flight from":flight.origin_country.name,
            "to": flight.destination_country.name,
            "date": flight.landing_time,
            # "image": flight.destination_country.image,
        })
     
    serializer = FlightSerializer(flight1, many=False)
    return Response(flight1)

@api_view(['GET'])
def getAllFlights(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''
    flights = Flights.objects.all()
    res= []
    for flight in flights:
        print(flight.destination_country)
        res.append({
            "ID": flight.id,
            "airline": flight.airline_company.name,
            "from":flight.origin_country.name,
            "to": flight.destination_country.name,
            "date": flight.landing_time,
            # "image": flight.destination_country.image
           
        })
        
    serializer = FlightSerializer(flights, many=True)
    return Response(res)


@api_view(['GET']) 
def getAirCompany(request,id):
    airlineCompany = Airline_Companies.objects.get(id=id)
    serializer = Airline_CompanySerializer(airlineCompany,many = False)
    return Response(serializer.data) 

@api_view(['GET'])
def getAllAirCompanies(request):
    airlineCompanies = Airline_Companies.objects.all()
    serializer = Airline_CompanySerializer(airlineCompanies, many=True)
    return Response(serializer.data)       