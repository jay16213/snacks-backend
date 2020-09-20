from django.contrib import admin

from .models import Snack, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'isAdmin')
    fieldsets = [
        (None,               {'fields': ['name', 'balance']}),
        ('Admin User', {'fields': ['isAdmin']}),
    ]

class SnackAdmin(admin.ModelAdmin):
    fields = ['name', 'amount', 'price']

admin.site.register(User, UserAdmin)
admin.site.register(Snack, SnackAdmin)
