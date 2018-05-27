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

Copy the `secret.json.sample` to `secret.json` and give fill it in with a key:

```bash
$ cp xkcdclone/xkcdclone/secret.json.sample xkcdclone/xkcdclone/secret.json
```

Finally, start up the server:

```bash
$ python xkcdclone/manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.
