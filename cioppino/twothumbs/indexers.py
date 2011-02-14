from plone.indexer.decorator import indexer
from zope.annotation.interfaces import IAnnotations
from interfaces import ILoveThumbsDontYou
from thumbconf import yays, nays


@indexer(ILoveThumbsDontYou)
def positive_ratings(object, **kw):
    annotations = IAnnotations(object)
    if annotations.has_key(yays):
        return len(annotations[yays])
        
    return 0