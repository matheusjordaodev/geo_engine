from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O nome de usuário é obrigatório')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    # Campos para controle de permissões
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'age']

    def __str__(self):
        return self.username

    # Métodos obrigatórios para o Django Admin
    def has_perm(self, perm, obj=None):
        """Verifica se o usuário tem permissão específica."""
        return True  # Ou implemente lógica personalizada de permissões

    def has_module_perms(self, app_label):
        """Verifica se o usuário tem permissão para ver o app 'app_label'."""
        return True

    @property
    def is_staff(self):
        """Se o usuário é membro da equipe, que pode acessar o Django Admin."""
        return self.is_admin
from django.db import models

class MenuEntry(models.Model):
    title = models.CharField(max_length=255)  # Título do item de menu
    url = models.CharField(max_length=255)    # URL que o item de menu deve apontar

    def __str__(self):
        return self.title
