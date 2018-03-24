from views import add_document, get_storage_info


def setup_routes(app):
    app.router.add_post('/add-document/', add_document)
    app.router.add_get('/storage-info/', get_storage_info)
