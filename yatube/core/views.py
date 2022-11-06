from django.shortcuts import render


def page_not_found(request, exception):
    template = 'core/404.html'
    return render(request, template, {'path': request.path}, status=404)


def csrf_failure(request, reason=''):
    template = 'core/403csrf.html'
    return render(request, template)


def internal_error(request, *args, **kwargs):
    template = 'core/500.html'
    return render(request, template)
