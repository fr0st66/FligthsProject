Nancys Flights progect- 

python manage.py runserver
roles = 

AnonymousUser -        not_authenticate
User -                 is_authenticate
Airline Company -      isAdminUser = is_staff
Administrator -        is_superUser

 after - login/logout- needed refresh

(*) python manage.py runserver

Full stack Flight-reservation app

# user - views2
    path('register/',views2.registerUser,name='register'),                                 test - DONE
    path('profile/',views2.getUser,name="user_profile"),                                   test done - regular login user + staff
    path('profile/update',views2.updateUserByUser,name="user_profile_apdate"),             test done- reg user + staff user
    path('login/', views2.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),      test done - by user / admin/ staff
    path('update/<id>/',views2.updateUserByAdmin,name="updateUser"),                       test- done by super user
    path('delete/id>/',views2.deleteUser,name="deleteUser"),                               test done by super user
    path('user/<id>', views2.getUserById, name='user'),                                    test done- by super user
    path('users/',views2.getUsers,name="users"),                                           test- done by super user

# order - views3
    path('add/',views3.addOrderTicket,name="orders-add"),
    path('order-all/', views3.getAllOrders, name='order'),                                test- done Staff                       
    path('order/', views3.getMyOrder, name='my_order'),                                   test done- login user + staff 
    path('order-delete/<id>', views3.deleteOrder, name='del_order'),                      test- done super user
    path('tickets/', views3.getMyTickets, name='tickets'),                                
    path('tickets-all/', views3.getAllTickets, name='all-tickets'),                       test- done super user

# bace - views1 - test - Done  
                                                                                           TEST- all Anounimos - DONE
# aircompanies - views4 
    path('create-flight/',views4.createFlight,name="create_flight"),                        test- done 
    path('update-flight/',views1.updateFlight,name="update_product"),                       test- done
    path('delete-flight/',views4.deleteFlight,name="delete_product"),                       test- done 
    path('add-airline/',views4.addNewAirCompany,name="add_airline"),                        test- done
    path('delete-airline/<id>',views4.deleteAirCompany,name="delete_airline"),              Test - done super user
 
]


tests - reguler user 
{
  "username": 
    "Emily"
  ,
  "password": 
    "em12345678"
  
}

staff 
{
  "username": 
    "user-denmark"
  ,
  "password": 
    "de12345678"
  
}
Super User
{
  "username": 
    "Nancy"
  ,
  "password": 
    "pel22fon"
  
}
