from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import category, category_info
from .form import CatCreateForm


class CatergoryTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="test123"
        )

    def test_created_categories(self):
        expected_categories = [
            "Bills",
            "Housing",
            "Transportation",
            "Groceries",
            "Entertainment",
        ]
        flag = self.client.login(username="testuser", password="test123")

        if flag:
            response = self.client.get(reverse("cat_list"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "category_list.html")
            for category in expected_categories:
                self.assertContains(response, category)

    def test_negative_budget(self):
        flag = self.client.login(username="testuser", password="test123")

        if flag:
            category_test = category.objects.filter(user=self.user).first()
            category_test.budget = -1000
            form = CatCreateForm(
                instance=category_test,
                data={"budget": category_test.budget, "name": category_test.name},
            )
            self.assertFalse(form.is_valid())

    def test_category_management(self):
        flag = self.client.login(username="testuser", password="test123")
        if flag:
            response = self.client.get(reverse("cat_list"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "category_list.html")

            # create category
            category_created = category.objects.create(
                user=self.user, name="test category", budget=1000
            )
            response = self.client.get(reverse("cat_list"))
            self.assertContains(response, "test category")
            self.assertContains(response, 1000)

            # update category
            category_created.name = "test1 category"
            category_created.budget = 2000
            category_created.save()
            response = self.client.get(reverse("cat_list"))
            self.assertContains(response, "test1 category")
            self.assertContains(response, 2000)

            # delete category
            category_created.delete()
            response = self.client.get(reverse("cat_list"))
            self.assertNotContains(response, "test1 category")
            self.assertNotContains(response, 2000)

    def test_expense_management(self):
        flag = self.client.login(username="testuser", password="test123")
        cat = category.objects.get(name="Bills", user=self.user)
        if flag:
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "category_info_list.html")

            # add expense
            category_info_created = category_info.objects.create(
                cat=cat, spend=1000, item="Electricity Bill", user=self.user
            )
            cat = category.objects.get(name="Bills", user=self.user)
            self.assertEqual(4000, cat.amt_left)

            # delete expense
            category_info_created.delete()
            cat = category.objects.get(name="Bills", user=self.user)
            self.assertEqual(5000, cat.amt_left)
