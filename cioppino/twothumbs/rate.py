from zope.annotation.interfaces import IAnnotations
from BTrees.OIBTree import OIBTree
from Products.CMFCore.utils import getToolByName


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

    if not yays in annotations:
        annotations[yays] = OIBTree()

    if not nays in annotations:
        annotations[nays] = OIBTree()

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
        userid = mtool.getAuthenticatedMember().id

    if userid in annotations[nays]:
        annotations[nays].pop(userid)

    if userid in annotations[yays]:
        annotations[yays].pop(userid)
        action = "undo"
    else:
        annotations[yays][userid] = 1
        action = "like"

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
    else:
        annotations[nays][userid] = 1
        action = "dislike"

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
    if yays in annotations:
        return len(annotations[yays])

    return 0
