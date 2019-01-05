Changelog
=========

2.1.2 (2019-01-05)
------------------

- Fix like/dislike inline popup text translations for composed language domains like nl-be.
  [fredvd]
- Prepare for Python 2 / 3 compatibility [Andreas Mantke]


2.1.1 (2016-09-12)
------------------

- Re-release 2.1.
  [timo]


2.1 (2016-09-12)
----------------

- Mv docs/HISTORY.txt -> CHANGES.rst to follow common best practice.
  [timo]

- Added upgrade for Plone 5 to recognize css- and js-file.
  [andreasma]

- Complete Plone 4 and Plone 5 compat using resource registries and splitted GS
  profiles
  [sneridagh]


2.0 (2016-03-09)
----------------

- Add compatability for Plone 5.
  [pbauer]

- Make visual appearance more discreet by moving the number of votes next to
  the thumbs and dropping the summary. Similar to the rating on youtube.
  [pbauer]

- HTML render fixes.
  [andreasma]

- Fix bug in like view that prevented authenticated user id from being used
  in votes when anonymous voting was enabled
  [cguardia]


1.8 (2014-11-07)
----------------
- allow anonyoums voting if configured (registry.xml) protected by weak
  cookie [jensens]
- fix duplicated ID for accessibility [simahawk]
- fix rendering under plone 4.3 [simahawk]
- feat: add event and triggers for content rules [Gagaro]
- qa: add travis and coverage support [toutp]
- qa: pep8 fixes [toutp,Gagaro,jensens]

1.7 (2013-06-04)
----------------
- Add french translation [toutpt]
- Make the template being 'index' to be customizable with zcml + browser layer
  [toutpt]
- Add catalan translation [mpampols]

1.6 (2012-06-11)
----------------
- Fix requirements for instances where dexterity is not installed [tschorr]

1.5 (2012-06-07)
----------------
- Add support for dexterity behaviors [eleddy]
- Fix confirmation message alignment for default plone sites [eleddy]

1.4 (2012-05-15)
----------------
- German translation added. [jensens]
- Added Brazilian Portuguese translation. [agnogueira]
- Add support for Plone 3 [rochecompaan]
- Enable use of the twotumbs widget outside the content div [rochecompaan]

1.3 (2011-09-22)
----------------
- Turn thumbs background images into a sprite [marcosfromero]
- Improve accessibility: non AJAX/JavaScript support [marcosfromero]
- Improve i18n and added new Spanish translations [marcosfromero]
- Improve feedback for anonymous users and after voting [marcosfromero]

1.2 (2011-05-27)
----------------
- Initial i18n and Spanish translation [hvelarde]


1.1 (2011-02-15)
----------------
- switch to absolute patch for form actions since it breaks when
  under the influence of rewriting [eleddy]


1 (2011-02-14)
--------------
- Initial release [eleddy on code, spanktar on graphics]
