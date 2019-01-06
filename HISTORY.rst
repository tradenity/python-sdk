.. :changelog:

History
-------

Version 0.1.2
-------------

* Workaround: move overridden __getitem__ from Base entity to Identifiable to work with django.
* Bug fix: fix Order#refund operation

Version 0.1.1
-------------

* Feature: New Exception: SessionExpiredException
* Feature: Add Tradenity.reset_current_session()
* Improvement: Add entity base class Identifiable
* Bug fix: LineItem.id always return None

Version 0.1.0
-------------

Initial release
