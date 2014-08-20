from interfaces import ILoveThumbsDontYou
from plone.indexer.decorator import indexer
import rate


@indexer(ILoveThumbsDontYou)
def positive_ratings(obj, **kw):
    return rate.getTotalPositiveRatings(obj)
