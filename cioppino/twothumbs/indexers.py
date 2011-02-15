from plone.indexer.decorator import indexer
from zope.annotation.interfaces import IAnnotations
from interfaces import ILoveThumbsDontYou
import rate


@indexer(ILoveThumbsDontYou)
def positive_ratings(object, **kw):
    return rate.getTotalPositiveRatings(object)