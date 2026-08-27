from django.http import Http404
from django.shortcuts import get_object_or_404 as _get_object_or_404


def get_object(model_or_queryset, /, **kwargs):
    """
    Thin wrapper around Django's get_object_or_404 with a name that reads
    better from service/selector code than the view-oriented original:

        item = get_object(InventoryItem, pk=item_id)

    Raising Http404 here is safe even outside a view — DRF's exception
    handler turns it into a proper 404 response.
    """
    try:
        return _get_object_or_404(model_or_queryset, **kwargs)
    except Http404:
        raise
