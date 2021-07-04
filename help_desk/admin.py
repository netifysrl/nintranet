from django.contrib import admin
from .models import Activity, Ticket
from registry.models import Customer, CustomerContact
from data_seeder.admin import DataGeneratorAdmin

# Register your models here.

#admin.site.register(Activity)
#admin.site.register(Customer)
#admin.site.register(Ticket)

admin.site.register(Customer, DataGeneratorAdmin)
admin.site.register(Ticket, DataGeneratorAdmin)
admin.site.register(Activity, DataGeneratorAdmin)
admin.site.register(CustomerContact, DataGeneratorAdmin)


