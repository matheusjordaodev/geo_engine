from django.contrib import admin
from .models.usuario import User
#from models.menu import MenuEntry

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',  'last_login')
    search_fields = ('username', 'cpf')


#admin.site.register(MenuEntry)