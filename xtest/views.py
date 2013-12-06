from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from pyramid.request import Request
from pyramid_handlers import action
from xtest.lib.BaseController import BaseController

from formencode import validators

class IndexController(BaseController):

    @action(renderer="json")
    def index(self,):
        return ['index']

    @action(renderer="json")
    def data(self, x=10):
        return range(0,int(x))

    @action(renderer="json", permission='admin')
    def secure(self):
        return ['ok']

    def xxx(self):
        return Response('secure1 ok')