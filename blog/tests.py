from django.test import TestCase, LiveServerTestCase, Client
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
        #self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        #self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        #self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        #self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        #self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        #self.assertEquals(only_post.pub_date.second, post.pub_date.second)

class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()


class AdminTest(BaseAcceptanceTest):
    fixtures = ['users.json']

    def test_login(self):
        # Get login page
        response = self.client.get('/adminlogin/?next=/admin')

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

        # Log the user in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/adminlogin/?next=/admin')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

    def test_logout(self):
        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/adminlogin/?next=/admin')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)