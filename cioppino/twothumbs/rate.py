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
    
    if not annotations.has_key(yays):
        annotations[yays] = OIBTree()
    
    if not annotations.has_key(nays):
        annotations[nays] = OIBTree()
        
    return annotations  


def loveIt(context, userid=None):
    """
    Like an item (context). If no user id is passed in, the logged in User 
    will be used. If the user has already commented in one place 
    or the other, remove that vote. Then add the new vote.
    """
    annotations = IAnnotations(context)
    
    if not userid:
        mtool =  getToolByName(context, 'portal_membership') 
        userid = mtool.getAuthenticatedMember().id

    if annotations[nays].has_key(userid):
        annotations[nays].pop(userid)

    annotations[yays][userid] = 1           
    context.reindexObject(idxs=['positive_ratings'])  
    
    
def hateIt(context, userid=None):
    """
    Dislike an item (context). If no user id is passed in, the logged in User 
    will be used.
    """
    annotations = IAnnotations(context)
    
    if not userid:
        mtool =  getToolByName(context, 'portal_membership') 
        userid = mtool.getAuthenticatedMember().id
    
    if annotations[yays].has_key(userid):
        annotations[yays].pop(userid)

    annotations[nays][userid] = 1  
    context.reindexObject(idxs=['positive_ratings'])  


def getTally(context):
    """
    Return a dictionary of total likes and dislikes
    """
    annotations = IAnnotations(context)
    return {
            'ups':len(annotations[yays]), 
            'downs': len(annotations[nays])
            }


def getMyVote(context, userid=None):
    """
    If the user liked this item, then return 1. If they 
    did not like it, -1, and if they didn't vote: 0.
    
    If no user is passed in, the logged in user will be returned
    """    
    annotations = IAnnotations(context)
    
    if not userid:
        mtool =  getToolByName(context, 'portal_membership') 
        userid = mtool.getAuthenticatedMember().id
    
    if annotations[yays].has_key(userid):
        return 1
        
    if annotations[nays].has_key(userid):
        return -1
        
    return 0
    
def getTotalPositiveRatings(context):
    """
    Return the total number of positive ratings
    """
    annotations = IAnnotations(context)
    if annotations.has_key(yays):
        return len(annotations[yays])
        
    return 0