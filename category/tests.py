from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import category, category_info


class CatergoryTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="test123"
        )
        cls.cat = category.objects.create(user=cls.user, name="Bills", budget=1000)
        cls.cat_info = category_info.objects.create(
            cat=cls.cat,
            spend=100,
            item="elect bill",
            user=cls.user,
        )

    def test_created_categories(self):
        flag = self.client.login(username="testuser", password="test123")

        if flag:
            response = self.client.get(reverse("cat_list"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "category_list.html")
            self.assertContains(response, "Bills")

    def test_created_category_info(self):
        flag = self.client.login(username="testuser", password="test123")
        if flag:
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "category_info_list.html")
            self.assertContains(response, "elect bill")
