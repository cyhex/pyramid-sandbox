__author__ = 'gx'

from pyramid.request import Request

class PylonsControllerViewMapper(object):
    def __init__(self, **kw):
        self.kw = kw

    def __call__(self, view):
        attr = self.kw['attr']
        def wrapper(context, request):
            matchdict = request.matchdict.copy()
            matchdict.pop('action', None)
            inst = view(request)
            meth = getattr(inst, attr)
            return meth(**matchdict)
        return wrapper


class BaseController(object):
    __view_mapper__ = PylonsControllerViewMapper
    __autoexpose__ = None

    def __init__(self, request):
        assert isinstance(request, Request)
        self.request = request
