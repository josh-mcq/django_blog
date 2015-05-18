from django.test import LiveServerTestCase, Client
from unittest import TestCase
from django.utils import timezone
from blog.models import Post, Category

# Create your tests here.
class PostTest(TestCase):
    def test_create_post(self):
        # Create the post
        post = Post()
        category = Category(id=1)

        # Set the attributes
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        category.title = 'My category'
        post.category = category

        # Save it
        post.save()

        # Check we can find it
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Check attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        #self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        #self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        #self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        #self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        #self.assertEquals(only_post.pub_date.second, post.pub_date.second)

class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

        # Create the new post
        self.client.post('/admin/blog/category/add/', {
            'title': 'Test Category',
            'slug':'test-category',
        },
        follow=True
        )


class AdminTest(BaseAcceptanceTest):
    fixtures = ['users.json']

    def test_login(self):
        # Get login page
        response = self.client.get('/admin/', follow=True)

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

        # Log the user in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

    def test_logout(self):
        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

    def test_create_post(self):
        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/blog/post/add/')
        self.assertEquals(response.status_code, 200)

        # Create a category
        self.client.post('/admin/blog/category/add/', {
            'title': 'Me Category',
            'slug':'me-category',
        },
        follow=True)

        response = self.client.post('/admin/blog/post/add/', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date': timezone.now(),
            'slug': 'my-first-post',
            'category': 2,
        },
        follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check added successfully
        self.assertTrue('added successfully' in response.content)

        # Check new post now in database
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)


    def test_create_category(self):
        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/blog/category/add/')
        self.assertEquals(response.status_code, 200)

        # Create the new post
        response = self.client.post('/admin/blog/category/add/', {
            'title': 'My Category',
            'slug':'my-category',
        },
        follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check added successfully
        self.assertTrue('added successfully' in response.content)

        # Check new post now in database
        all_posts = Category.objects.all()
        self.assertEquals(len(all_posts), 1)
