from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from cioppino.twothumbs import rate
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import json
            

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
        portal_state = getMultiAdapter((self.context,self.request), name='plone_portal_state')        
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
    form = self.request.form
    if form.get('form.lovinit', False):
        rate.loveIt(self.context)
    elif form.get('form.hatedit', False):
        rate.hateIt(self.context)
    else:
        return "We don't like ambiguity around here. Check yo self before you wreck yo self."
    
    tally = rate.getTally(self.context)
    RESPONSE.setHeader('Content-Type', 'application/javascript')       
    return json.dumps(tally)
    