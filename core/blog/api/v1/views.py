
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response # type: ignore


@api_view()
def postlist(request):
    return Response('ok')

