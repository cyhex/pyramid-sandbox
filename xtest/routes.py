__author__ = 'gx'

def add_routes(config):

    #static
    config.add_static_view('static', 'static', cache_max_age=3600)

    # add handler for user with user permission for all actions
    config.add_handler('user', '/user/{action}', handler='xtest.controllers.user.UserController', permission='user')

    # add root controller
    config.add_handler('index', '/', handler='xtest.controllers.root.RootController', action='index')
    config.add_handler('data', '/data/{x:.*}', handler='xtest.controllers.root.RootController', action='data')
    config.add_handler('varible', '/varible.{ext}', handler='xtest.controllers.root.RootController', action='varible')
    config.add_handler('default', '/{action}', handler='xtest.controllers.root.RootController')
