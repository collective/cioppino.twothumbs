from zope.component.interfaces import ObjectEvent
from zope import interface


class ILikeEvent(interface.Interface):
    """Interface for the Like event"""


class LikeEvent(ObjectEvent):
    interface.implements(ILikeEvent)


class IUnlikeEvent(interface.Interface):
    """Interface for the Unlike event"""


class UnlikeEvent(ObjectEvent):
    interface.implements(IUnlikeEvent)


class IDislikeEvent(interface.Interface):
    """Interface for the Dislike event"""


class DislikeEvent(ObjectEvent):
    interface.implements(IDislikeEvent)


class IUndislikeEvent(interface.Interface):
    """Interface for the Undislike event"""


class UndislikeEvent(ObjectEvent):
    interface.implements(IUndislikeEvent)
