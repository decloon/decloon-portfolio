import os, unittest
os.environ["TESTING"] = "true"          # Must be set before importing app
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # ---------- Home page ----------
    def test_home(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)
        self.assertIn("<title>Declan&#39;s Portfolio</title>", html)
        self.assertIn("Timeline", html)

    # ---------- /api/timeline_post happy path ----------
    def test_timeline_api_happy_path(self):
        # should start empty
        res = self.client.get("/api/timeline_post")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["timeline_posts"], [])

        # insert one post
        res = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["name"], "John Doe")

        # check GET now returns exactly one
        res = self.client.get("/api/timeline_post")
        self.assertEqual(len(res.get_json()["timeline_posts"]), 1)

    # ---------- Timeline HTML page ----------
    def test_timeline_page(self):
        res = self.client.get("/timeline")
        self.assertEqual(res.status_code, 200)
        self.assertIn("<title>Timeline</title>", res.get_data(as_text=True))

    # ---------- malformed requests ----------
    def test_malformed_timeline_post(self):
        # missing name
        res = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(res.status_code, 400)
        self.assertIn("Invalid name", res.get_data(as_text=True))

        # empty content
        res = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        self.assertEqual(res.status_code, 400)
        self.assertIn("Invalid content", res.get_data(as_text=True))

        # bad email
        res = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(res.status_code, 400)
        self.assertIn("Invalid email", res.get_data(as_text=True)) 