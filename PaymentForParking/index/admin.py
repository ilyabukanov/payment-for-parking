from django.contrib import admin
from .models import Parking,tickets,paidparking,paidseasontickets

class IndexAdmin(admin.ModelAdmin):
    list_display = ('adress', 'workinghours', 'minimaltimeforpayment', 'price', 'numberofavailableseats', 'Абонементы')
    list_display_links = ('adress',)
    search_fields = ('adress','workinghours')

    def Абонементы(self, obj):
        return ', '.join(obj.tickets.values_list('nameseasontickets', flat=True))

class ticketsAdmin(admin.ModelAdmin):
    list_display = ('nameseasontickets','numberofdays', 'time', 'price')
    list_display_links = ('nameseasontickets',)
    search_fields = ('nameseasontickets',)

class paidparkingAdmin(admin.ModelAdmin):
        list_display = ('adress', 'carnumber', 'amountoftime', 'price', 'telephone','datetimepaidparking')
        list_display_links = ('adress',)
        search_fields = ('carnumber',)

class paidseasonticketsAdmin(admin.ModelAdmin):
        list_display = ('nametickets','carnumber','price','telephone','datetimepaidtickets')
        list_display_links = ('nametickets',)
        search_fields = ('carnumber',)

admin.site.register(Parking, IndexAdmin)
admin.site.register(tickets, ticketsAdmin)
admin.site.register(paidparking, paidparkingAdmin)
admin.site.register(paidseasontickets,paidseasonticketsAdmin)
