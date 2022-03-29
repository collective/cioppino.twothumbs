# -*- coding: utf-8 -*-
from zope.interface import implementer
from zope.interface.interfaces import IObjectEvent
from zope.interface.interfaces import ObjectEvent


class ILikeEvent(IObjectEvent):
    """Interface for the Like event"""


@implementer(ILikeEvent)
class LikeEvent(ObjectEvent):
    """Like Event"""


class IUnlikeEvent(IObjectEvent):
    """Interface for the Unlike event"""


@implementer(IUnlikeEvent)
class UnlikeEvent(ObjectEvent):
    """Unlike Event"""


class IDislikeEvent(IObjectEvent):
    """Interface for the Dislike event"""


@implementer(IDislikeEvent)
class DislikeEvent(ObjectEvent):
    """Displike Event"""


class IUndislikeEvent(IObjectEvent):
    """Interface for the Undislike event"""


@implementer(IUndislikeEvent)
class UndislikeEvent(ObjectEvent):
    """Undislike Event"""
