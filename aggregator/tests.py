from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Episode


class AggregatorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.episode = Episode.objects.create(
            podcast_name="The Real Python Test Podcast",
            title="The one on testing",
            description="This is a sample description of this epsiode",
            pub_date=timezone.now(),
            link="https://realpython.com/podcasts/rpp/82/",
            image="https://files.realpython.com/media/real-python-logo-square.28474fda9228.png",
            guid="79ed3544-31be-45ab-b1a1-0f1de80a0353",

        )

    def test_post_model(self):
        self.assertEqual(self.episode.title, "The one on testing")
        self.assertEqual(self.episode.description, "This is a sample description of this epsiode")
        self.assertEqual(str(self.episode), "The Real Python Test Podcast: The one on testing")
        self.assertEqual(self.episode.link, "https://realpython.com/podcasts/rpp/82/")
        self.assertEqual(self.episode.guid, "79ed3544-31be-45ab-b1a1-0f1de80a0353")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_urlname_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Podregator</title>')
        self.assertTemplateUsed(response, 'homepage.html')
