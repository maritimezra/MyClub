from django.test import TestCase

from .models import Member


class MemberTestCase(TestCase):

    def setUp(self):
        self.member = Member.objects.create(
            first_name="John", last_name="Doe", email="john@example.com"
        )

    def test_get_full_name(self):
        self.assertEqual(self.member.get_full_name(), "John Doe")

    def test_get_short_name(self):
        self.assertEqual(self.member.get_short_name(), "John")

    def test_get_member_with_id(self):
        retrieved_member = Member.get_member_with_id(self.member.id)
        self.assertEqual(retrieved_member, self.member)

    def test_get_member_with_email(self):
        retrieved_member = Member.get_member_with_email(self.member.email)
        self.assertEqual(retrieved_member, self.member)

    def test_get_member_with_first_name(self):
        retrieved_member = Member.get_member_with_first_name(self.member.first_name)
        self.assertEqual(retrieved_member, self.member)

    def test_get_member_with_last_name(self):
        retrieved_member = Member.get_member_with_last_name(self.member.last_name)
        self.assertEqual(retrieved_member, self.member)

    def test_create_member(self):
        new_member = Member.create_member("jane@example.com", "Jane", "Doe")
        self.assertIsNotNone(new_member)
        self.assertEqual(new_member.email, "jane@example.com")
        self.assertEqual(new_member.first_name, "Jane")
        self.assertEqual(new_member.last_name, "Doe")

    def test_update_member(self):
        updated_member = Member.update_member(self.member.email, "Jane", "Smith")
        self.assertIsNotNone(updated_member)
        self.assertEqual(updated_member.first_name, "Jane")
        self.assertEqual(updated_member.last_name, "Smith")

    def test_delete_member(self):
        Member.delete_member(self.member.email)
        self.assertIsNone(Member.get_member_with_email(self.member.email))
