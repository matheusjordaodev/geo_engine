from django.contrib import admin
from .models import User
from .models import MenuEntry
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'cpf', 'age', 'date_created', 'last_login')
    search_fields = ('username', 'cpf')


admin.site.register(MenuEntry)