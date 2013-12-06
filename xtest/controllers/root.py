__author__ = 'gx'

from pyramid.response import Response
from pyramid_handlers import action
from xtest.controllers import BaseController

class RootController(BaseController):

    def index(self,):
        return Response('ok')

    @action(renderer="json")
    def data(self, x=10):

        print self.request.GET
        print self.request.params.getall('x')
        return range(0, int(x))

    # we can limit access based on permission on action
    @action(renderer="json", permission='admin')
    def secure(self):
        return ['ok']

    def xxx(self):
        return Response('secure1 ok')
