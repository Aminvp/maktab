from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Post, User, Comment, Category
from django.urls import reverse
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key


class PostsTest(APITestCase):
    def setUp(self):
        user = User(username='akbar', password='1234')
        user.save()
        self.posts = mommy.make(Post, __fill__optional=True, _quantity=3)
        self.post = Post(id=1)

    def tearDown(self):
        print('Done ...')

    def test_posts(self):
        url = reverse('blog:post_list')

        resp = self.client.get(url)

        print(resp.json())

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 3)


class CommentsTest(APITestCase):
    def setUp(self):
        self.comment = mommy.make(Comment, __fill__optional=True, _quantity=4)

    def tearDown(self):
        print('Done ...')

    def test_comments(self):
        url = reverse('blog:comment_list')
        resp = self.client.get(url)

        print(resp.json())

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 4)


class CategoriesTest(APITestCase):
    def setUp(self):
        self.category = mommy.make(Category, __fill__optional=True, _quantity=2)

    def tearDown(self):
        print('Done ...')

    def test_categories(self):
        url = reverse('blog:category_list')
        resp = self.client.get(url)

        print(resp.json())

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 2)