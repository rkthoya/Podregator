import logging

from django.core.management.base import BaseCommand
from django.conf import settings

import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from aggregator.models import Episode


logger = logging.getLogger(__name__)


def save_new_episodes(rss_feed):
    podcast_title = rss_feed.feed.title
    podcast_image = rss_feed.feed.image["href"]

    for entry in rss_feed.entries[:36]:
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


def delete_old_job_executions(max_age=604800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            fetch_stackoverflow_episodes,
            trigger="interval",
            hours=120,
            id="The Stack Overflow Podcast",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The Stack Overflow Podcast")

        scheduler.add_job(
            fetch_thl_episodes,
            trigger="interval",
            hours=168,
            id="The Happiness Lab",
            max_instances=1,
            replace_existing=True,
        )


        scheduler.add_job(
            fetch_pythonbytes_episodes,
            trigger="interval",
            hours=120,
            id="Python Bytes",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: Python Bytes Feed.")

        scheduler.add_job(
            fetch_tkp_episodes,
            trigger="interval",
            hours=336,
            id="The Knowledge Project",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The Knowledge Project Podcast.")

        scheduler.add_job(
            fetch_codenewbie_episodes,
            trigger="interval",
            hours=168,
            id="The CodeNewbie Podcast",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The CodeNewbie Podcast.")

        scheduler.add_job(
            fetch_freakonomics_episodes,
            trigger="interval",
            hours=168,
            id="Freakonomics Radio",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: Freakonomics Radio.")

        scheduler.add_job(
            fetch_realpython_episodes,
            trigger="interval",
            hours=168,
            id="The Real Python Podcast",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The Real Python Podcast.")

        scheduler.add_job(
            fetch_djangochat_episodes,
            trigger="interval",
            hours=168,
            id="Django Chat",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: Django Chat.")

        scheduler.add_job(
            fetch_tiu_episodes,
            trigger="interval",
            hours=168,
            id="This Is Uncomfortable",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: This is Uncomfortable.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added Weekly Job: Delete Old Job Executions from the Database.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
