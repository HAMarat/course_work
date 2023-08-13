from django.contrib import admin
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ("last_name", "first_name")

    def __str__(self):
        return self.username


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "username")
    list_filter = ("is_staff", "is_active", "is_superuser")
    exclude = ('password',)
    readonly_fields = ("last_login", "date_joined")
