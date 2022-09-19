from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Posts
from api.serializer import PostSerializer,UserSerializer,CommentSerializer
from rest_framework import authentication,permissions
from rest_framework.decorators import action



# Create your views here


class PostsView(ViewSet):
    authentication_classes =[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Posts.objects.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        serializer=PostSerializer(qs)
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        serializer=PostSerializer(instance=qs,data=request.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Posts.objects.get(id=id)
        serializer=PostSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})
class UserView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class PostmodelView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer=PostSerializer(data=request.data,context={"usr":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    @action(methods=["GET"],detail=False)
    def my_posts(self,request,*args,**kwargs):
        user=request.user
        qs=user.post.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)
    @action(methods=["GET"],detail=True)
    def get_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        commet=post.comments_set.all()
        serilizer=CommentSerializer(commet,many=True)
        return Response(data=serilizer.data)
    @action(methods=["POST"],detail=True)
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Posts.objects.get(id=id)
        serializer=CommentSerializer(data=request.data,context={"user":request.user,"post":pst})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["POST"],detail=True)
    def add_like(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Posts.objects.get(id=id)
        user=request.user
        pst.liked_by.add(user)
        return Response(data="ok Liked")

    @action(methods=["GET"],detail=True)
    def get_likes(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Posts.objects.get(id=id)
        cnt=pst.liked_by.all().count()
        return Response(data=cnt)
