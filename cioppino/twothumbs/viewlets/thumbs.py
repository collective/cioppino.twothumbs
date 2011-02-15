from zope.interface import implements
from zope.component import getMultiAdapter
from AccessControl import getSecurityManager
from zope.viewlet.interfaces import IViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotations


class ThumbsViewlet(BrowserView):
    """
    Render the thumbs view, but using the viewlet arch
    """
    implements(IViewlet)
    render = ViewPageTemplateFile('templates/thumbs_viewlet.pt')

    def __init__(self, context, request, view=None, manager=None):
        super(ThumbsViewlet, self).__init__(context, request)
        self.context = context
        

        
