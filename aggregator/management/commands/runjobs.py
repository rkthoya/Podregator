from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser

from aggregator.models import Episode


def save_new_episodes(rss_feed):
    podcast_title = rss_feed.feed.title
    podcast_image = rss_feed.feed.image["href"]

    for entry in rss_feed.entries:
        if not Episode.objects.filter(guid=entry.guid).exists():
            episode = Episode(
                title=entry.title,
                description=entry.description,
                pub_date=parser.parse(entry.published),
                link=entry.link,
                image=podcast_image,
                podcast_name=podcast_title,
                guid=entry.guid,
            )
            episode.save()


def fetch_stackoverflow_episodes():
    feed = feedparser.parse("https://feeds.simplecast.com/XA_851k3")
    save_new_episodes(feed)


def fetch_tkp_episodes():
    feed = feedparser.parse("https://theknowledgeproject.libsyn.com/rss")
    save_new_episodes(feed)


def fetch_codenewbie_episodes():
    feed = feedparser.parse("http://feeds.codenewbie.org/cnpodcast.xml")
    save_new_episodes(feed)


def fetch_djangochat_episodes():
    feed = feedparser.parse("https://feeds.simplecast.com/WpQaX_cs")
    save_new_episodes(feed)


def fetch_tnbi_episodes():
    feed = feedparser.parse("https://feeds.megaphone.fm/LI1683199352")
    save_new_episodes(feed)


def fetch_tiu_episodes():
    feed = feedparser.parse("https://www.marketplace.org/feed/podcast/this-is-uncomfortable-reema-khrais")
    save_new_episodes(feed)


def fetch_pythonbytes_episodes():
    feed = feedparser.parse("https://pythonbytes.fm/episodes/rss")
    save_new_episodes(feed)


def fetch_realpython_episodes():
    feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(feed)


def fetch_thl_episodes():
    feed = feedparser.parse("https://omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/96C5C41E-0BC8-4661-B184-AE32006CD726/D623EF0B-3FEE-4C26-B815-AE32006CD739/podcast.rss")
    save_new_episodes(feed)


def fetch_freakonomics_episodes():
    feed = feedparser.parse("https://feeds.simplecast.com/Y8lFbOT4")
    save_new_episodes(feed)


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_stackoverflow_episodes()
        fetch_realpython_episodes()
        fetch_thl_episodes()
        fetch_tkp_episodes()
        fetch_freakonomics_episodes()
        fetch_pythonbytes_episodes()
        fetch_codenewbie_episodes()
        fetch_djangochat_episodes()
        fetch_tnbi_episodes()
        fetch_tiu_episodes()
