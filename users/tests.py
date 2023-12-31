from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(username="Lolala", name="Lolita", password="lolipoli", bio="Love to cook but eat even more", email="lola@bola.com")

    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("username").max_length
        self.assertEqual(max_length, 120)

    def test_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 120)
    
    def test_bio_string(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.bio, "Love to cook but eat even more")