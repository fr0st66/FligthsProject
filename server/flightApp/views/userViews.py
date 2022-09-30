
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from ..serailizers import UserSerializerWithToken, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer 

@api_view(['GET'])
def getRoutes(request):
    routes =[
        '/flight/',
        '/flight/<id>',
        '/user',
        '/user/register',
        '/user/login',
        '/user/profile',
    ]
    return Response(routes)


# (1 user)____________________________________________________________________________

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            password = make_password(data['password']),
        )
        serializer = UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message = {"detail":"User with this email all ready exist"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

# permision - login user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    user =request.user 
    serializer = UserSerializer(user,many = False)
    return Response(serializer.data)  

# permision - Super user   
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data)

# permision - login user
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserByUser(request):
    user =request.user 
    serializer = UserSerializerWithToken(user,many = False)
    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    if data['password'] !="":
        user.password= make_password(data['password'])
    user.save()
    return Response(serializer.data)

# permision - Super user  
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateUserByAdmin(request,id):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    user =User.objects.get(id=id)
    data = request.data
    user.first_name = data['name']
    user.username = data['username']
    user.email = data['email']
    user.is_staff = data['isAdmin']
    user.save()
    serializer = UserSerializer(user,many = False)
    return Response(serializer.data)

# permision - Super user  
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request,id):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    temp = User.objects.get(id=id)
    temp.delete()
    return Response("User was deleted")     

# permision - Super user  
@api_view(['GET']) 
@permission_classes([IsAdminUser])
def getUserById(request,id):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    users = User.objects.get(id=id)
    serializer = UserSerializer(users,many = False)
    return Response(serializer.data) 

# permision - Super user  
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserByUsername(request,username):
    if not request.user.is_superuser :
        return Response({'detail': 'Not Authorized - permission only to Admin Super User '},
            status=status.HTTP_401_UNAUTHORIZED)
    users = User.objects.get(username=username)
    serializer = UserSerializer(users,many = False)
    return Response(serializer.data)   