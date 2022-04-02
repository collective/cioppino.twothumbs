Changelog
=========

2.2.4 (2022-04-02)
------------------

- Fix registry uninstall profile for Plone 5 [andreasma]


2.2.3 (2022-03-31)
------------------

- Flake8 and isort fixes [andreasma]
- Add buildout scripts for Plone 5.2 and Plone 6.0 and
  add them to the Github actions test matrix (instead of
  former test_plone.5.2.x buildout file [andreasma]
- Use plone.api for user actions [andreasma]
- Remove Travis configuration / buildout file [andreasma]
- Update localization files [andreasma]


2.2.2 (2022-03-21)
------------------

- Import IObjectEvent and ObjectEvent from zope.interface.interfaces
  [andreasma]
- Change buildout scripts (buildout.cfg, base.cfg) and add new file
  constraints_plone52.txt and new buildout script test_plone-5.2.x.cfg
  [andreasma]
- Add lib64 to .gitignore [andreasma]
- Update requirements.txt to use constraints_plone52.txt [andreasma]
- Fix import exception in like.py and flake8 fix in testing.py [andreasma]
- Update Manifest.in [andreasma]
- Add Github actions workflow with tests [andreasma]


2.2.1 (2021-11-22)
------------------

- Add name to behavior.
  [pbauer]

- Prevent csrf-confirmation when initializing annotations.
  [pbauer]
  

2.2.0 (2019-10-09)
------------------

- Register collection criterions for our positive ratings field.
  Using it as a sorting criterion works.
  Using it as a selection criterion (X thumbs or less/more than X thumbs)
  needs a `fix in plone.app.querystring <https://github.com/plone/plone.app.querystring/issues/93>`_,
  specifically version 1.2.13 (Plone 4) or 1.4.12 (Plone 5.1) or higher.
  [maurits]

- Fixed error: nulltranslate has no "context" argument.
  Fixes `issue 24 <https://github.com/collective/cioppino.twothumbs/issues/24>`_.
  [maurits]


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
