# Podregator
A content aggregator for some of my favorite podcasts.

## Features
* RSS Feed Parsing using the [feedparser library](https://feedparser.readthedocs.io/en/latest/).
* Custom [django-admin](https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/) command.
* Task scheduling using [Advanced Python Scheduler](https://apscheduler.readthedocs.io/en/stable/) and [django-apscheduler](https://github.com/jcass77/django-apscheduler).
* Unit tests.
* Logging.

## Running the project locally.
To run the code locally ensure you have git and Python 3.8 or above installed. It'll be also helpful to have [Pipenv](https://pypi.org/project/pipenv/) installed. Clone the repo into your computer through:

`git clone https://github.com/rkthoya/Podregator.git`

While inside the repo install the project dependencies using

`pipenv install`

Activate your virtual environment:

`pipenv shell`

Run the migrations to create a simple SQLite database:

`python manage.py migrate`

To see a demo of parsed episodes on the homepage you might need to alter the time interval between a task's execution. You can do this in the aggregator/management/commands/runjobs.py. In the `handle()` method of the `Command` class, change the "hours" argument in any of the `scheduler.add_job()` functions to minutes. For example:

```python
scheduler.add_job(
            fetch_stackoverflow_episodes,
            trigger="interval",
            # hours=120,
            minutes=2,
            id="The Stack Overflow Podcast",
            max_instances=1,
            replace_existing=True,
        )
```

You'll need two separate terminals - both in the same virtual environment - to run the development server and scheduled tasks:

`python manage.py runserver`

`python manage.py runjobs`
