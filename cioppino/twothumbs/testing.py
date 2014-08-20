from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig


class TwoThumbs(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cioppino.twothumbs
        xmlconfig.file('configure.zcml',
                       cioppino.twothumbs,
                       context=configurationContext
                       )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cioppino.twothumbs:default')

TWOTHUMBS_FIXTURE = TwoThumbs()
TWOTHUMBS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TWOTHUMBS_FIXTURE,),
    name="TwoThumbs:Integration"
)
