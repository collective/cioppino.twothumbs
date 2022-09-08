from Products.CMFPlone import interfaces as Plone
from Products.CMFQuickInstallerTool import interfaces as QuickInstaller
from zope.interface import implementer


@implementer(Plone.INonInstallable)
class HiddenProfiles:

    def getNonInstallableProfiles(self):
        """Do not show on Plone's list of installable profiles."""
        return [
            'cioppino.twothumbs:install-base',
            'cioppino.twothumbs:uninstall',
            'cioppino.twothumbs:uninstall-base',
        ]


@implementer(QuickInstaller.INonInstallable)
class HiddenProducts:

    def getNonInstallableProducts(self):
        """Do not show on QuickInstaller's list of installable products."""
        return []
