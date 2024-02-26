from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(null=True, max_length=16)
    date_joined = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name or self.email.split("@")[0]

    def get_member_with_id(id):
        return Member.objects.filter(id=id).first()

    def get_member_with_email(email):
        return Member.objects.filter(email=email).first()

    def get_member_with_first_name(first_name):
        return Member.objects.filter(first_name=first_name).first()

    def get_member_with_last_name(last_name):
        return Member.objects.filter(last_name=last_name).first()

    def create_member(email, first_name, last_name):
        member = Member.objects.create(
            email=email, first_name=first_name, last_name=last_name
        )
        member.save()
        return member

    def update_member(email, first_name=None, last_name=None):
        member = Member.get_member_with_email(email)
        if member:
            if first_name:
                member.first_name = first_name
            if last_name:
                member.last_name = last_name
            member.save()
            return member
        return None

    def delete_member(email):
        member = Member.get_member_with_email(email)
        if member:
            member.delete()
