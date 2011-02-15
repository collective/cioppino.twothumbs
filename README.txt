Introduction
============
This will add those terribly "delish" little thumbs all over facebook 
to products of your choosing. By default, only logged in users can rate 
a product, and once they are logged in they can vote once (and change 
their vote at any time)


Installation
------------
Your mission, should you choose to accept it is to add the package to 
your buildout config and rerun buildout. If you want it as a viewlet 
below the content title, you must follow the viewlet directions below 
before restarting and installing. Otherwise install immediately and then 
skip to the section on browser views.

As a Viewlet
------------
Then, in the configure.zcml 
in the base of your product you need to tell which content types should 
display the thumbs. For example, with the PloneSoftwareCenter product, 
the configure.zcml has the lines::

    <include package="cioppino.twothumbs" />
    <class class=".content.project.PSCProject">
       <implements interface="cioppino.twothumbs.interfaces.ILoveThumbsDontYou" />
    </class>
    
That little diddy would add the thumbs viewlet to the PSCProject 
product only. You only need to include the package 1 time but you 
need to add the class block for every content type you would like 
to show the thumbs.

As a Browser View
-----------------
Additionally, you can generate the widget on any content page in any place
by just adding a few lines to your template::
    
    <div tal:content="structure here/@@rate-if-you-dare"/>


Migration
---------
If you used to use plone.contentratings and want to migrate to the thumbs 
product, there is an example in the trunk of PloneSoftwareCenter. It's 
pretty easy. Please see http://svn.plone.org/svn/collective/Products.PloneSoftwareCenter/tags/1.6.1/Products/PloneSoftwareCenter/Extensions/migrateratings.py for an example.


Bugs/Suggestions/Help
---------------------
Please file bugs at https://github.com/eleddy/cioppino.twothumbs.


Credits
-------
This product was initially developed at the Plone Cioppino Sprint in 
Bodega Bay 2011. The source code is filled with plenty of inside jokes 
and may only be maintainable after drinking copious numbers of 
Manhattans. Without the [drink] support of everyone there, this may not 
have been made possible. Big ups.