import unittest
from blogpost.models import User, Blog, Comment
from blogpost import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_alexmuliande = User(username = "alexmunliande", password = "minayojane", email="alexnad425@gmail.com")
        self.new_blog = Blog(title="code", body = "coding rocks", user_id =self.user_alexmuliande.id )
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()



    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'code')
        self.assertEquals(self.new_blog.body,"coding rocks")
        self.assertEquals(self.new_blog.user_id, self.user_alexmuliande.id)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blogs(self):

        self.new_blog.save_blog()
        blogs = Blog.get_blogs()
        self.assertTrue(len(blogs)==1)