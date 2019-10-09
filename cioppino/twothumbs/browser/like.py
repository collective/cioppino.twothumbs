try:
    import json
except:
    # fallback to simplejson for pre python2.6
    import simplejson as json
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from cioppino.twothumbs import _
from cioppino.twothumbs import rate
from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.i18n.interfaces import ITranslationDomain
from uuid import uuid4

COOKIENAME = 'yolikeitorhateit'


def nulltranslate(msgid, *args, **kwargs):
    """Workaround for non-registered translation domain to prevent breaking.
    """
    return msgid


class LikeWidgetView(BrowserView):
    """ Display the like/unlike widget. """
    index = ViewPageTemplateFile('templates/thumbs.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.annotations = rate.setupAnnotations(self.context)

    def __call__(self):
        return self.index()

    def canRate(self):
        registry = getUtility(IRegistry)
        if registry.get('cioppino.twothumbs.anonymousvoting', False):
            return True
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
        portal_state = getMultiAdapter((self.context, self.request),
                                       name='plone_portal_state')
        anonuid = None
        if portal_state.anonymous():
            anonuid = self.request.cookies.get(COOKIENAME, None)
        return rate.getMyVote(self.context, userid=anonuid)


class LikeThisShizzleView(BrowserView):
    """ Update the like/unlike status of a product via AJAX """

    def __call__(self, REQUEST, RESPONSE):
        registry = getUtility(IRegistry)
        anonuid = None
        anonymous_voting = registry.get('cioppino.twothumbs.anonymousvoting', False)
        portal_state = getMultiAdapter((self.context, self.request),
                                       name='plone_portal_state')

        if portal_state.anonymous():
            if not anonymous_voting:
                return RESPONSE.redirect('%s/login?came_from=%s' %
                                         (portal_state.portal_url(),
                                          REQUEST['HTTP_REFERER'])
                                         )
            else:
                anonuid = self.request.cookies.get(COOKIENAME, None)
                if anonuid is None:
                    anonuid = str(uuid4())
                    RESPONSE.setCookie(COOKIENAME, anonuid)

        form = self.request.form
        action = None
        if form.get('form.lovinit', False):
            action = rate.loveIt(self.context, userid=anonuid)
        elif form.get('form.hatedit', False):
            action = rate.hateIt(self.context, userid=anonuid)
        else:
            return _(u"We don't like ambiguity around here. Check yo self "
                     "before you wreck yo self.")

        if not form.get('ajax', False):
            return RESPONSE.redirect(REQUEST['HTTP_REFERER'])
        else:
            tally = rate.getTally(self.context)
            tally['action'] = action

            # Create handy translate function
            translate = self._get_translator()

            tally['msg'] = translate(
                self._getMessage(action),
                context=self.request
            )
            tally['close'] = translate(
                _(u"Close"),
                context=self.request
            )

            RESPONSE.setHeader('Content-Type',
                               'application/json; charset=utf-8')
            response_json = json.dumps(tally)
            RESPONSE.setHeader('content-length', len(response_json))
            return response_json

    def _get_translator(self):
        """returns a callable acting as a translator
        """
        td = queryUtility(ITranslationDomain, name='cioppino.twothumbs')
        if td:
            return td.translate

        return nulltranslate

    def _getMessage(self, action):
        if (action == 'like'):
            return _(u"You liked this. Thanks for the feedback!")
        elif (action == 'dislike'):
            return _(u"You dislike this. Thanks for the feedback!")
        elif (action == 'undo'):
            return _(u"Your vote has been removed.")
