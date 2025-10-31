
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response # type: ignore
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status # type: ignore
from django.shortcuts import get_object_or_404


@api_view()
def postList(request):
    return Response('ok')

@api_view()
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    serializer=PostSerializer(post)
    return Response(serializer.data)
   


