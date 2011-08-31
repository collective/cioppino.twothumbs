#!/bin/bash

# Don't forget to activate your i18ndude workingenv before running this
# script if you have such a thing.

# Edit this to wherever your i18ndude lives, or trust the path.
I18NDUDE="../../../../bin/i18ndude"
PRODUCTNAME="cioppino.twothumbs"
I18NDOMAIN=$PRODUCTNAME

# Synchronise the .pot with the templates.

$I18NDUDE rebuild-pot --pot locales/${PRODUCTNAME}.pot --create ${I18NDOMAIN} .

# Synchronise the resulting .pot with all .po files.
for po in locales/*/LC_MESSAGES/${PRODUCTNAME}.po; do
    $I18NDUDE sync --pot locales/${PRODUCTNAME}.pot $po
done
