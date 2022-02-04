# Django Channels

Channels augments Django to bring WebSocket, long-poll HTTP, task offloading and other async support to your code, using familiar Django design patterns and a flexible underlying framework that lets you not only customize behaviours but also write support for your own protocols and needs

Documentation, installation and getting started instructions are at https://channels.readthedocs.io

Channels is an official Django Project and as such has a deprecation policy. Details about what's deprecated or pending deprecation for each release is in the release notes.

Support can be obtained through several locations - see our support docs for more.

You can install channels from PyPI as the channels package. See our installation and tutorial docs for more.

#Dependencies
All Channels projects currently support Python 3.6 and up. channels is compatible with Django 2.2 and 3.2.

WebSocket King
https://websocketking.com/

Maintenance and Security
To report security issues, please contact security@djangoproject.com. For GPG signatures and more security process information, see https://docs.djangoproject.com/en/dev/internals/security/.

To report bugs or request new features, please open a new GitHub issue. For larger discussions, please post to the django-developers mailing list.

Maintenance is overseen by Carlton Gibson with help from others. It is a best-effort basis - we unfortunately can only dedicate guaranteed time to fixing security holes.

If you are interested in joining the maintenance team, please read more about contributing and get in touch!

Other Projects
The Channels project is made up of several packages; the others are:

#Daphne, the HTTP and Websocket termination server
#channels_redis, the Redis channel backend
$asgiref, the base ASGI library/memory backend

@jitendra-meena
