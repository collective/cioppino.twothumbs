from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer
from zope.viewlet.interfaces import IViewlet


@implementer(IViewlet)
class ThumbsViewlet(BrowserView):
    """
    Render the thumbs view, but using the viewlet arch
    """
    render = ViewPageTemplateFile('templates/thumbs_viewlet.pt')

    def __init__(self, context, request, view=None, manager=None):
        super(ThumbsViewlet, self).__init__(context, request)
        self.context = context
