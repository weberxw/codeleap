from django.shortcuts import render
from careers.models import Post
from careers.serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response


class Posts(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 200)
        return Response(serializer.errors, status=400)

    def get(self, request, pk=None):
        if pk:
            try:
                queryset = self.queryset.get(id=pk)
                many = False
            except:
                return Response('Post não encontrado.', status = 400)
        else:
            queryset = self.queryset.all()
            many = True

        serializer = self.serializer_class(queryset, many=many)
        return Response(serializer.data, status = 200)

    def patch(self, request, pk):
        try:
            data = request.data
            post = self.queryset.get(id=pk)
        except:
            return Response('Post não encontrado.', status = 400)
        if data.get('title'):
            post.title = data['title']
        if data.get('content'):
            post.content = data['content']
        
        post.save()
            
        serializer = self.serializer_class(post, many=False)
        return Response(serializer.data, status = 200)