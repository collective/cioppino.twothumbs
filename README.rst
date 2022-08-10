Introduction
============
This will add those terribly "delish" little thumbs all over facebook
to products of your choosing. By default, only logged in users can rate
a product, and once they are logged in they can vote once (and change
their vote at any time)


Installation
------------

.. image:: https://coveralls.io/repos/collective/cioppino.twothumbs/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/collective/cioppino.twothumbs


Your mission, should you choose to accept it is to add the package to
your buildout config and rerun buildout. If you want it as a viewlet
below the content title, you must follow the viewlet directions below
before restarting and installing. Otherwise install immediately and then
skip to the section on browser views.

Make sure you have installed or "Activated" the product if things aren't
working as expected.


Compatibility
-------------

cioppino.twothumbs works with Plone 5.2 and 6.0, on Python 3 only.
For other Plone and Python versions, see the 2.x releases.


As a Viewlet
------------

Cioppino.TwoThumbs provides a behavior for dexterity content types. In
the dexterity configuration UI, it will be listed under "Behaviors".

You may also manually add this behavior to your type by adding the following
to ``../path/to/profiles/default/types/your_type.xml``::

    ...
    <property name="behaviors">
        <element value="cioppino.twothumbs" />
        ...
    </property>
    ...


As a Browser View
-----------------
Additionally, you can generate the widget on any content page in any place
by just adding a few lines to your template::

    <div tal:content="structure here/@@rate-if-you-dare"/>

Note that this ONLY works if the browser view is in context of a content
type since it requires access to content object annotations.


Migration
---------
If you used to use plone.contentratings and want to migrate to the thumbs
product, there is an example in PloneSoftwareCenter. It's
pretty easy. Please see https://github.com/collective/Products.PloneSoftwareCenter/blob/master/Products/PloneSoftwareCenter/Extensions/migrateratings.py for an example.
It has not been tried on Python 3 though, so maybe you need to migrate to a version supporting Python 2 first.
But it is okay to try.

Anonymous Voting
----------------
Anonymous voting is possible, but **weak**. A unique identifier is
generated and set as cookie on first vote. Then the uid is used as
identifier for later display/changes. To enable anonymous voting go to
Plones configuration registry, search for ``cioppino.twothumbs.anonymous``
entry and edit it. Alternativly you can add your own ``registry.xml`` to
your sites profile::

    <?xml version="1.0"?>
    <registry>
        <record name="cioppino.twothumbs.anonymousvoting">
            <value>True</value>
        </record>
    </registry>

It's easy to fake anonymous votes, so don't trust them much. A todo here
is to add a captcha, which would make automated vote-faking impossible.


Bugs/Suggestions/Help
---------------------
Please file bugs at https://github.com/collective/cioppino.twothumbs.


Credits
-------
This product was initially developed at the Plone Cioppino Sprint in
Bodega Bay 2011. The source code is filled with plenty of inside jokes
and may only be maintainable after drinking copious numbers of
Manhattans. Without the [drink] support of everyone there, this may not
have been made possible. Big ups.
