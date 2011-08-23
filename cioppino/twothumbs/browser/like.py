import json
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from cioppino.twothumbs import _
from cioppino.twothumbs import rate


class LikeWidgetView(BrowserView):
    """ Display the like/unlike widget. """
    render = ViewPageTemplateFile('templates/thumbs.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.annotations = rate.setupAnnotations(self.context)

    def __call__(self):
        return self.render()

    def canRate(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name='plone_portal_state')
        return not portal_state.anonymous()

    def getStats(self):
        """
        Look up the annotation on the object and return the number of
        likes and hates
        """
        return rate.getTally(self.context)

    def myVote(self):
        if not self.canRate():
            return 0

        return rate.getMyVote(self.context)


class LikeThisShizzleView(BrowserView):
    """ Update the like/unlike status of a product via AJAX """

    def __call__(self, REQUEST, RESPONSE):

        # First check if the user is allowed to rate
        portal_state = getMultiAdapter((self.context, self.request),
                                       name='plone_portal_state')
        if portal_state.anonymous():
            return RESPONSE.redirect('%s/login?came_from=%s' % (portal_state.portal_url(), REQUEST['HTTP_REFERER']))


        form = self.request.form
        action = None
        if form.get('form.lovinit', False):
            action = rate.loveIt(self.context)
        elif form.get('form.hatedit', False):
            action = rate.hateIt(self.context)
        else:
            return _(u"We don't like ambiguity around here. Check yo self before you wreck yo self.")

        if not form.get('ajax', False):
            return RESPONSE.redirect(REQUEST['HTTP_REFERER'])
        else:
            tally = rate.getTally(self.context)
            tally['action'] = action
            if(action=='like'):
                tally['msg'] = _(u"You liked this. Thanks for the feedback!")
            elif(action=='dislike'):
                tally['msg'] = _(u"You dislike this. Thanks for the feedback!")
            elif(action=='undo'):
                tally['msg'] = _(u"Your vote has been removed.")
            
            RESPONSE.setHeader('Content-Type', 'application/json; charset=utf-8')
            response_json = json.dumps(tally)
            RESPONSE.setHeader('content-length', len(response_json))
            return response_json
