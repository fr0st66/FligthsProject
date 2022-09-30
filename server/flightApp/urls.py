from django.urls import path
from flightApp.views import baseViews as views1
from flightApp.views import userViews as views2
from flightApp.views import orderViews as views3
from flightApp.views import airlineViews as views4


app_name= 'flightApp' 
urlpatterns = [

# user - views2
    path('register/', views2.registerUser, name='register'),
    path('profile/',views2.getUser,name="user_profile"),
    path('profile/update',views2.updateUserByUser,name="user_profile_apdate"),
    path('login/', views2.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('update/<id>/',views2.updateUserByAdmin,name="updateUser"),
    path('delete/<id>/',views2.deleteUser,name="deleteUser"),
    path('user/<id>', views2.getUserById, name='user'),
    path('users/',views2.getUsers,name="users"),

# order - views3
    path('add/',views3.addOrderTicket,name="orders-add"),
    path('order-all/', views3.getAllOrders, name='order'),
    path('tickets/', views3.getMyTickets, name='tickets'),
    path('tickets-all/', views3.getAllTickets, name='all-tickets'),
    path('order/', views3.getMyOrder, name='my_order'),
    path('order-delete/<id>', views3.deleteOrder, name='del_order'),

# bace - views1
    path('', views1.getAllFlights, name='flight_list'),
    path('country/', views1.getAllCountries, name='country'), 
    path('country/<id>', views1.getCountry, name='country'),
    path('airline/', views1.getAllAirCompanies, name='airline-company'),
    path('airline/<id>', views1.getAirCompany, name='airline-company'),
    path('flight/', views1.getAllFlights, name='all_flights'),
    path('flight/<id>', views1.getFlight, name='flight'),

# aircompanies - views4 
    path('create-flight/',views4.createFlight,name="create_flight"),
    path('update-flight/<id>',views4.updateFlight,name="update_flight"),
    path('delete-flight/<id>',views4.deleteFlight,name="delete_flight"),
    path('add-airline/',views4.addAirCompany,name="add_airline"),
    path('delete-airline/<id>',views4.deleteAirCompany,name="delete_airline"),
 
]
