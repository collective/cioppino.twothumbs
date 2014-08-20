from zope import interface
from zope.component.interfaces import IObjectEvent
from zope.component.interfaces import ObjectEvent


class ILikeEvent(IObjectEvent):
    """Interface for the Like event"""


class LikeEvent(ObjectEvent):
    interface.implements(ILikeEvent)


class IUnlikeEvent(IObjectEvent):
    """Interface for the Unlike event"""


class UnlikeEvent(ObjectEvent):
    interface.implements(IUnlikeEvent)


class IDislikeEvent(IObjectEvent):
    """Interface for the Dislike event"""


class DislikeEvent(ObjectEvent):
    interface.implements(IDislikeEvent)


class IUndislikeEvent(IObjectEvent):
    """Interface for the Undislike event"""


class UndislikeEvent(ObjectEvent):
    interface.implements(IUndislikeEvent)
