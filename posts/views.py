from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from  . models import Post
from . serializers import PostSerializer
class PostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,post_pk):
        try:
            post = Post.objects.get(pk=post_pk,user = request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
        #     return HttpResponse(serializer.data)
        # return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
    def get(self,request):
        post = Post.objects.filter(is_active = True)
        serializer = PostSerializer(post,many = True)
        return Response(serializer.data)
        