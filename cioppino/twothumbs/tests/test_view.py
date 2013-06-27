import unittest2 as unittest

from cioppino.twothumbs.testing import TWOTHUMBS_INTEGRATION_TESTING

class TestView(unittest.TestCase):

    layer = TWOTHUMBS_INTEGRATION_TESTING

    def test_view_render(self):
        portal = self.layer['portal']
        view = portal.restrictedTraverse('@@rate-if-you-dare')
        self.assertTrue('value="Ugh"' in view())
