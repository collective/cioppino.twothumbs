# fallback to simplejson for pre python2.6
try:
    import json
except:
    import simplejson as json
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter, queryUtility
from zope.i18n.interfaces import ITranslationDomain
from Products.CMFCore.utils import getToolByName
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

            # Create handy translate function
            td = queryUtility(ITranslationDomain, name='cioppino.twothumbs')
            if td:
                tx = td.translate
            else:
                # Workaround for non-registered translation domain to prevent breaking
                def tx(msgid, target_language=None):
                    return msgid

            ltool = getToolByName(self, 'portal_languages')
            target_language = ltool.getPreferredLanguage()

            if(action=='like'):
                tally['msg'] = tx(_(u"You liked this. Thanks for the feedback!"), target_language=target_language)
            elif(action=='dislike'):
                tally['msg'] = tx(_(u"You dislike this. Thanks for the feedback!"), target_language=target_language)
            elif(action=='undo'):
                tally['msg'] = tx(_(u"Your vote has been removed."), target_language=target_language)

            tally['close'] = tx(_(u"Close"), target_language=target_language)
            
            RESPONSE.setHeader('Content-Type', 'application/json; charset=utf-8')
            response_json = json.dumps(tally)
            RESPONSE.setHeader('content-length', len(response_json))
            return response_json
