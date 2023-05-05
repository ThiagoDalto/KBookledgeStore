# KBookledgeStore

Kbookledge is a platform that allows independent book authors to publish and sell their independent books online, allowing access and purchase of books by new readers.
You can view use instructions here in the official documentation: [Documentation](https://web-production-544c.up.railway.app/api/docs/)

## Our mission


With the crisis in the publishing sector, authors of independent books were the ones who suffered the most difficulties to publish their works.
So, a platform for buying and selling virtual books was thought up, where readers can access offers and promotions. We allow the publication of books by any user, as long as he is registered as an author. Other users can search and purchase these books.

## Installing

1. Create a virtual environment with ```Python```
```Bash
$ python -m venv venv
```

2. Install app dependencies ```pip```
```Bash
$ pip install -r requirements.txt
```

3. Generate and run the migrations
```Bash
$ python manage.py makemigrations
$ python manage.py migrate
```

4. Start App
```Bash
$ python manage.py runserver
```

## Tests
The tests were written with pytest
```Bash
$ pytest testdox --vvs
```
