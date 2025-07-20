import unittest
from peewee import SqliteDatabase
from app import TimelinePost

MODELS = [TimelinePost]
test_db = SqliteDatabase(":memory:")

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post_crud(self):
        p1 = TimelinePost.create(
            name="John Doe",
            email="john@example.com",
            content="Hello world, I'm John!"
        )
        self.assertEqual(p1.id, 1)

        p2 = TimelinePost.create(
            name="Jane Doe",
            email="jane@example.com",
            content="Hello world, I'm Jane!"
        )
        self.assertEqual(p2.id, 2)

        posts = list(TimelinePost.select().order_by(TimelinePost.id))
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].name, "John Doe")
        self.assertEqual(posts[1].email, "jane@example.com") 