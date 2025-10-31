
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response # type: ignore
from .serializers import PostSerializer
from ...models import Post



@api_view()
def postList(request):
    return Response('ok')

@api_view()
def postDetail(request,id):
    post = Post.objects.get(pk=id)
    print(post.__dict__)
    serializer=PostSerializer(post)
    print(serializer.data)
    return Response(serializer.data)


