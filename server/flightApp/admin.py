from django.contrib import admin

from .models import Flights, Countries, Order,Tickets,Airline_Companies

admin.site.register(Flights)
admin.site.register(Countries)
admin.site.register(Tickets)
admin.site.register(Airline_Companies)
admin.site.register(Order)




