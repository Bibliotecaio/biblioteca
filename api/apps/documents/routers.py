from rest_framework.routers import Route, SimpleRouter


class DetailRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}',
            mapping={'get': 'retrieve'},
            name='{basename}',
            initkwargs={'suffix': 'Detail'}
        )
    ]


class ListRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}',
            mapping={'get': 'list'},
            name='{basename}',
            initkwargs={'suffix': 'List'}
        )
    ]
