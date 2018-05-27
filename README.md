# django-xkcd-clone

This repo re-creates [xkcd.com](https://xkcd.com)'s main page as a Django app.

![](https://github.com/andy-esch/django-xkcd-clone/blob/master/xkcd-django-clone.gif?raw=true)

## Getting going

Clone this repo and move into it:

```bash
$ git clone https://github.com/andy-esch/django-xkcd-clone.git
$ cd django-xkcd-clone
```

Create a virtual environment with Python 3, install the requirements in a virtual environment, and activate the shell. Here I use [`pipenv`](https://docs.pipenv.org/).

```bash
$ pipenv --three
$ pipenv -r requirements.txt
$ pipenv shell
```

Start up the server:

```bash
$ python xkcdclone/manage.py runserver
```

Open `http://localhost:8000` in your browser.
