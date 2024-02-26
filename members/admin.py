from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "date_joined",
    )


admin.site.register(Member, MemberAdmin)
