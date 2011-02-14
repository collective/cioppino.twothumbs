from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from AccessControl import getSecurityManager
from zope.annotation.interfaces import IAnnotations
from BTrees.OIBTree import OIBTree
from cioppino.twothumbs.thumbconf import yays, nays
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import json


class LikeWidgetView(BrowserView):  
  """ Display the like/unlike widget. """
  render = ViewPageTemplateFile('templates/thumbs.pt')
  
  def __init__(self, context, request):
        self.context = context
        self.request = request
        self.annotations = IAnnotations(self.context)
    
        # set up the annotation if it hasn't been set up already
        if not self.annotations.has_key(yays):
            self.annotations[yays] = OIBTree()
        
        if not self.annotations.has_key(nays):
            self.annotations[nays] = OIBTree()  
  
  def __call__(self):
    return self.render()
      
  def canRate(self):  
        portal_state = getMultiAdapter((self.context,self.request), name='plone_portal_state')        
        return not portal_state.anonymous()
    
  def getStats(self):
        """
        Look up the annotation on the object and return the number of
        likes and hates 
        """

        return { "thumbsup": len(self.annotations[yays]), 
                 "thumbsdown": len(self.annotations[nays]),
                }
                
  def myVote(self):
    """
    If the currently logged in user liked this item, then return 1. If they 
    did not like it, -1, and if they didn't vote: 0.
    """    
    if not self.canRate():
        return 0
        
    mtool =  getToolByName(self, 'portal_membership') 
    userid = mtool.getAuthenticatedMember().id
    
    if self.annotations[yays].has_key(userid):
        return 1
        
    if self.annotations[nays].has_key(userid):
        return -1
        
    return 0
                
        
class LikeThisShizzleView(BrowserView): 
  """ Update the like/unlike status of a product via AJAX """ 
  
  def __call__(self, REQUEST, RESPONSE):
    form = self.request.form
    love = form.get('form.lovinit', False)  
    hate = form.get('form.hatedit', False)  
    
    if not(love or hate):
        return "We don't like ambiguity around here. Check yo self before you wreck yo self."
    
    annotations = IAnnotations(self.context)
    
    mtool =  getToolByName(self, 'portal_membership') 
    userid = mtool.getAuthenticatedMember().id
    
    """
    if the user has already commented in one place 
    or the other, remove that vote. Then add the 
    new vote.
    """ 
    if love and annotations[nays].has_key(userid):
        annotations[nays].pop(userid)
    if hate and annotations[yays].has_key(userid):
        annotations[yays].pop(userid)
    if hate:
        annotations[nays][userid] = 1
    if love: 
        annotations[yays][userid] = 1       
    
    self.context.reindexObject(idxs=['positive_ratings'])    
    
    RESPONSE.setHeader('Content-Type', 'application/javascript')
    
    tally = {
            'ups':len(annotations[yays]), 
            'downs': len(annotations[nays])
            }
            
    return json.dumps(tally)
    