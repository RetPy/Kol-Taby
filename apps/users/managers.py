from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, alias, password, **extra_fields):
        if not alias:
            raise ValueError("User must have an alias")
        user = self.model(alias=alias, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, alias, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(alias, password, **extra_fields)
