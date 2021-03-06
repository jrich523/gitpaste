from helpers import has_access_to_paste
from models import Set, Paste, Commit
from django.shortcuts import get_object_or_404, redirect


def private(model, function=None):

    def decorator(view_func):
        def _wrapped_view(request, pk, *args, **kwargs):
            result = get_object_or_404(model, pk=pk)
            paste_set = None

            if model == Set:
                paste_set = result
            elif model == Commit:
                paste_set = result.parent_set
            elif model == Paste:
                paste_set = result.revision.parent_set

            if has_access_to_paste(request, paste_set, kwargs.get('private_key')):
                return view_func(request, pk, result, *args, **kwargs)
            return redirect('paste')

        return _wrapped_view

    if function:
        return decorator(function)
    return decorator
