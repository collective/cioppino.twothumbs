from plone.app.contentrules.handlers import execute


def like(event):
    obj = event.object
    execute(obj, event)


def unlike(event):
    obj = event.object
    execute(obj, event)


def dislike(event):
    obj = event.object
    execute(obj, event)


def undislike(event):
    obj = event.object
    execute(obj, event)
