# Notes

Some explanatory notes in case this is the first Django 
application you've encountered.

## Django

- Django has a settings configuration file in 
`/geneology/settings.py`. 
That's for things like setting up the database,
authentication system, file uploads and such.
- The `View` functions are all subclasses of Django's
generic class-based views, and they live in
`/familyinfo/views.py`. Mostly what they're about
is the mechanics of a simple CRUD application
(Create, Retrieve, Update, Delete records).
- Django is using something called an Object-Relational 
Mapping (`ORM`) so that I'm throwing around Python objects
without having to worry about how the database stores or
retrieves them (i.e. I don't have to write any `SQL`).
- The data objects I'm throwing around are defined in
`/familyinfo/models.py`. Notice that Django model classes, 
for convenience, use a slightly different syntax for declaring 
fields as data members of the classes, compared to standard
Python.

Roughly speaking, here's the order of events.
- the request comes in from a browser
- Django looks at the request's path (`/home`, `/foo/bar`, etc.)
- It matches that path against a set of regexes in 
`geneology` and chooses a `View` function.
- It's the `View` function that then has to 
inspect the request, do whatever calculation,
render the data to HTML using an HTML template,
and return it as an HTTP Response.
- I can restrict who gets to which view, so it's pretty
easy to set this up such that you have to sign in
to create, edit, or delete data, but not to list or
retrieve data.
