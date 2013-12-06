from pyramid.config import Configurator
from xtest.views import IndexController
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.include("pyramid_handlers")
    config.add_handler('index', '/', handler=IndexController, action='index')
    config.add_handler('data', '/data/{x:.*}', handler=IndexController, action='data')
    config.add_handler('default', '/{action}', handler=IndexController)
    config.scan()
    return config.make_wsgi_app()
