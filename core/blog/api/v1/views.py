from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework import viewsets  # type: ignore
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # type: ignore
from rest_framework import mixins  # type: ignore
from rest_framework.decorators import action  # type: ignore
from rest_framework.filters import SearchFilter, OrderingFilter  # type: ignore
from rest_framework.decorators import api_view, permission_classes  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category


# Example for function based view
"""
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":        
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)"""


#####

# Example for APIView in Class Based View
'''class PostList(APIView):
    """getting a list of posts and creating new post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self,request):
        # retrieving a list of posts
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """ creating a post with providing data """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''


'''class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self,request,id):
        """ retrieving the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """ editing the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        """ deleting the post object """
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)
'''

'''
#class PostList(ListCreateAPIView):
    #""" getting a list of posts and creating new post """
   # permission_classes = [IsAuthenticatedOrReadOnly]
    #serializer_class = PostSerializer
    #queryset = Post.objects.filter(status=True)'''

'''#class PostDetail(RetrieveUpdateDestroyAPIView):
    #""" getting detail of the post and edit plus removing it """
    #permission_classes = [IsAuthenticatedOrReadOnly]
    #serializer_class = PostSerializer
    #queryset = Post.objects.filter(status=True)'''


# Example for ViewSet in CBV


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
