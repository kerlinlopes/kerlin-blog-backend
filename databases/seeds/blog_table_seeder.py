"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Breakfast", "body": "eat breakfast"})
        Blog.create({"title": "Lunch", "body": "eat Lunch"})
        Blog.create({"title": "dinner", "body": "eat dinner"})