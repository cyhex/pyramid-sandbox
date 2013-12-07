__author__ = 'gx'

from pyramid.response import Response
from pyramid_handlers import action
from xtest.controllers import BaseController
from formencode import validators
from xtest.lib.decorators import validate

class RootController(BaseController):

    @action(renderer="templates/tmpl.pt")
    def index(self):
        return {}

    @action(renderer="json")
    def data(self, x=10):
        return range(0, int(x))

    # we can limit access based on permission on action
    @action(renderer="json", permission='admin')
    def secure(self):
        return ['ok']

    def xxx(self):
        raise Exception('Not Exposed')

    @action(renderer="templates/d.pt", match_param='ext=html')
    @action(renderer="json", match_param='ext=json')
    def varible(self, ext):
        """
        Variable response renderer from match_param (route needed to get ext from url)
        http://0.0.0.0:6543/varible.json
        http://0.0.0.0:6543/varible.html
        """
        data = {'d':range(0, 10)}
        return data

    @action(renderer="templates/d.pt", request_param='html')
    @action(renderer="json", request_param='json')
    @action(renderer="json")
    def varible_request(self):
        """
        Variable response renderer from request_param (no route needed)
        http://0.0.0.0:6543/varible_request?json
        http://0.0.0.0:6543/varible_request?html
        http://0.0.0.0:6543/varible_request - default json

        """
        data = {'d':range(0, 10)}
        return data


    @action(renderer="json")
    def cust_header(self):
        self.request.response.status_code = 201
        return {'ok':1}


    @action(renderer='json')
    @validate(validators={'i': validators.Int(), 's': validators.String(strip=True), 'f': validators.Bool()})
    def validate(self, i, s, f):
        return [i,s,f]