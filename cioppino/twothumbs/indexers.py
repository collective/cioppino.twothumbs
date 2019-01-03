from cioppino.twothumbs.interfaces import ILoveThumbsDontYou
from plone.indexer.decorator import indexer
import cioppino.twothumbs.rate as rate


@indexer(ILoveThumbsDontYou)
def positive_ratings(obj, **kw):
    return rate.getTotalPositiveRatings(obj)
