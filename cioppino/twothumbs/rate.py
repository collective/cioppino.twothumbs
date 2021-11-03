from BTrees.OIBTree import OIBTree
from cioppino.twothumbs.event import DislikeEvent
from cioppino.twothumbs.event import LikeEvent
from cioppino.twothumbs.event import UndislikeEvent
from cioppino.twothumbs.event import UnlikeEvent
from plone.protect.interfaces import IDisableCSRFProtection
from Products.CMFCore.utils import getToolByName
from zope import event
from zope.annotation.interfaces import IAnnotations
from zope.globalrequest import getRequest
from zope.interface.declarations import alsoProvides


# The name of the annotation fields, namespaces so
# we can avoid conflicts
yays = 'cioppino.twothumbs.yays'
nays = 'cioppino.twothumbs.nays'


def setupAnnotations(context):
    """
    set up the annotations if they haven't been set up
    already. The rest of the functions in here assume that
    this has already been set up
    """
    annotations = IAnnotations(context)
    changed = False
    if yays not in annotations:
        annotations[yays] = OIBTree()
        changed = True

    if nays not in annotations:
        annotations[nays] = OIBTree()
        changed = True

    if changed:
        request = getRequest()
        alsoProvides(request, IDisableCSRFProtection)

    return annotations


def loveIt(context, userid=None):
    """
    Like an item (context). If no user id is passed in, the logged in User
    will be used. If the user has already liked the item, remove the vote.
    If the user has already disliked the item, remove that vote and add a
    new 'like' one.
    """
    annotations = IAnnotations(context)
    action = None

    if not userid:
        mtool = getToolByName(context, 'portal_membership')
        if mtool.isAnonymousUser():
            raise ValueError('userid must be passed activly for anon users')
        userid = mtool.getAuthenticatedMember().id
    if userid in annotations[nays]:
        annotations[nays].pop(userid)

    if userid in annotations[yays]:
        annotations[yays].pop(userid)
        action = "undo"
        event.notify(UnlikeEvent(context))
    else:
        annotations[yays][userid] = 1
        action = "like"
        event.notify(LikeEvent(context))

    context.reindexObject(idxs=['positive_ratings'])
    return action


def hateIt(context, userid=None):
    """
    Dislike an item (context). If no user id is passed in, the logged in User
    will be used.
    """
    annotations = IAnnotations(context)
    action = None

    if not userid:
        mtool = getToolByName(context, 'portal_membership')
        userid = mtool.getAuthenticatedMember().id

    if userid in annotations[yays]:
        annotations[yays].pop(userid)

    if userid in annotations[nays]:
        annotations[nays].pop(userid)
        action = "undo"
        event.notify(UndislikeEvent(context))
    else:
        annotations[nays][userid] = 1
        action = "dislike"
        event.notify(DislikeEvent(context))

    context.reindexObject(idxs=['positive_ratings'])
    return action


def getTally(context):
    """
    Return a dictionary of total likes and dislikes
    """
    setupAnnotations(context)
    annotations = IAnnotations(context)
    return {
        'ups': len(annotations[yays]),
        'downs': len(annotations[nays]),
        'mine': getMyVote(context)
    }


def getMyVote(context, userid=None):
    """
    If the user liked this item, then return 1. If they
    did not like it, -1, and if they didn't vote: 0.

    If no user is passed in, the logged in user will be returned
    """
    annotations = IAnnotations(context)

    if not userid:
        mtool = getToolByName(context, 'portal_membership')
        userid = mtool.getAuthenticatedMember().id

    if userid in annotations[yays]:
        return 1

    if userid in annotations[nays]:
        return -1

    return 0


def getTotalPositiveRatings(context):
    """
    Return the total number of positive ratings
    """
    annotations = IAnnotations(context)
    return len(annotations.get(yays, {}))
