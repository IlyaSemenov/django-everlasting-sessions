django-everlasting-sessions
===========================

This Django middleware prevents user sessions from expiration.


Problem
=======

When using ``django.contrib.sessions.middleware.SessionMiddleware``, Django only saves the session cookie when a session is modified. On a typical site that only happens when a user logs in. In two weeks this session cookie expires and the user is prompted to login again, even if he's been actively using the site.


Solution
========

**django-everlasting-sessions** provides a middleware that will update session cookies once in a while (every day by default), provided there is some activity from the user.


Installation
============

::

	pip install django-everlasting-sessions


Usage
=====

Add the middleware to ``settings.py``:

.. code:: python

	MIDDLEWARE_CLASSES = [
		...
		'django.contrib.sessions.middleware.SessionMiddleware',
		'django_everlasting_sessions.UpdateSessionMiddleware',  # Must go after SessionMiddleware
		...
	]


The rest will happen automatically.


Options
=======

The following default is used which you can override in ``settings.py``:

.. code:: python

	SESSION_COOKIE_REFRESH = 86400  # Interval in seconds.
