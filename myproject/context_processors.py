def breadcrumbs(request):
    path = [p for p in request.path_info.split('/') if p]
    
    if not path or path[0].lower() == 'home':
        request.session['breadcrumbs'] = []
        breadcrumbs = [{'name': 'Home', 'url': '/'}]
    else:
        if not request.session.get('breadcrumbs'):
            request.session['breadcrumbs'] = [{'name': 'Home', 'url': '/'}]
        breadcrumbs = request.session['breadcrumbs']
        for i in range(len(path)):
            breadcrumb = {'name': path[i].capitalize(), 'url': '/' + '/'.join(path[:i+1])}
            if breadcrumb not in breadcrumbs:
                breadcrumbs.append(breadcrumb)
    
    request.session['breadcrumbs'] = breadcrumbs
    return {'breadcrumbs': breadcrumbs}
