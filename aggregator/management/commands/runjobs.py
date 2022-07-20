from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser

from aggregator.models import Episode


class Command(BaseCommand):
    def handle(self, *args, **options):
        _feed = feedparser.parse("https://feeds.simplecast.com/XA_851k3")
        podcast_title = _feed.feed.title
        podcast_image = _feed.feed.image["href"]

        for entry in _feed.entries:
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
