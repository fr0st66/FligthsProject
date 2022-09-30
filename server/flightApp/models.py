from django.db import models
from django.contrib.auth.models import User 


class Countries (models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(upload_to='static',null=True,blank=True,default='/israel.jpg')
    def __str__(self):
        return self.name


# __________________________________________________________________________________________  
# staff

class Airline_Companies (models.Model):
    name = models.CharField(unique=True, max_length=100)   
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name              
# ______________________________________________________________________________________________________________
# product

class Flights (models.Model): 
    airline_company = models.ForeignKey(Airline_Companies, on_delete=models.CASCADE)
    origin_country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='origin')
    destination_country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(editable=True)
    landing_time = models.DateTimeField(editable=True)
    remaining_tickets = models.IntegerField()

    def __str__(self):
        return '{} {} ' .format( str(self .remaining_tickets), str(self. origin_country),str(self. destination_country) )

# _________________________________________________________________________________________________________________
# customers

class Order (models.Model):
    first_name = models.CharField(max_length=40) 
    last_name = models.CharField(max_length=40)  
    address = models.CharField(max_length=100)  
    phone_no = models.CharField(unique=True, max_length=12)
    credit_card = models.CharField(unique=True, max_length=40)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
#_______________________________________________________________________________________________
# order item

class Tickets (models.Model):
    flight = models.OneToOneField(Flights, on_delete=models.CASCADE, unique=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return  '{} {}'.format(self.flight, self.order, self.order.first_name,self.flight.airline_company )
