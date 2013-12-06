__author__ = 'gx'

from pyramid.response import Response
from pyramid_handlers import action
from xtest.controllers import BaseController
from pyramid.view import view_defaults

class UserController(BaseController):

    @action(renderer="json")
    def index(self,):
        return ['user index']

    @action(renderer="json")
    def list(self,):
        return ['user list']
