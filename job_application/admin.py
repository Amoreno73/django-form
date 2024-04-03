from django.contrib import admin
from .models import Form

# this inherits from admin.ModelAdmin
# we will be able to create and modify admin interfaces
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email") #display func for django interface
    search_fields = ("first_name", "last_name", "email") #we have created a django search func
    list_filter = ("date", "occupation")
    ordering = ("-first_name",) #tuple -> ordering by name alphabetically
    # "-" to sort in the reverse order
    readonly_fields = ("occupation",) # now you cannot change occupation field manually
    

# Register your models here.
admin.site.register(Form, FormAdmin)




# left off on slide 234