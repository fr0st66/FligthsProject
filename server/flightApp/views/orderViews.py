
from rest_framework.decorators import api_view
from ..models import Order, Tickets, Flights
from ..serailizers import  OrderSerializer, TicketsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

# permision - login user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderTicket(request):
    user = request.user
    data = request.data
    orderTicket = data['orderTicket']
    order = Order.objects.create(
            user=user,
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            phone_no=data['phone_no'],
            credit_card=data['credit_card'],
        )

    for item in orderTicket:
            flight = Flights.objects.get(id=item['flight'])
            Tickets.objects.create(
                flight=flight,
                order=order
            )
            # to remove flight from מלאי
            flight.remaining_tickets -= 1
            Flights.save()

    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


# permision - login user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrder(request):
    user =request.user
    order = user.order_set.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)
    
# permision - login user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyTickets(request):
    user =request.user
    tickets = user.order_set.all()
    serializer = TicketsSerializer(tickets, many=True)
    return Response(serializer.data) 

# permision - Super user only
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAllTickets(request):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    tickets = Tickets.objects.all()
    serializer = TicketsSerializer(tickets, many=True)
    return Response(serializer.data)       

# permission - Super user only
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAllOrders(request):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# permision - Super user only
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteOrder(request,id):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    temp = Order.objects.get(id=id)
    temp.delete()
    return Response("Order was deleted")


