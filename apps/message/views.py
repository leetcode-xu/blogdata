from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from account.models import User
from .models import Message
# Create your views here.

# class AuthUser(BaseAuthentication):
#
#     def authenticate(self, request):
#         if request.user.is_anonymous:
#             raise exceptions.AuthenticationFailed('未登录状态')
#         else:
#             return request.user, None


class RootSer(ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Message
        fields = "__all__"
        depth = 2


class MsgSer(ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    root_comment = RootSer(many=True, write_only=True)

    class Meta:
        model = Message
        depth = 2
        fields = '__all__'


class MsgPage(PageNumberPagination):

    max_page_size = 50
    page_size = 50
    page_query_param = 'page'
    page_size_query_param = 'size'


class MsgTree:

    def get_dispose(self):
        self.one = []
        self.two= []
        for msg in self.msg_ser:
            if not msg['root']:
                self.one.append(msg)
            else:
                self.two.append(msg)
        return self.one

    def get_msgtree(self,obj):
        try:
            self.msg_all = Message.objects.all().order_by('-create_time')
            self.msg_page = MsgPage().paginate_queryset(queryset=self.msg_all, request=obj.request, view=obj)
            if len(self.msg_page) <= 1:
                self.msg_ser = [MsgSer(instance=self.msg_page[0], many=False).data]
            else:
                self.msg_ser = MsgSer(instance=self.msg_page, many=True).data
            return self.get_dispose()
        except Exception as e:
            print(str(e))
            return []


# url: /m/gbook/
class GbookView(APIView):
    # authentication_classes = [AuthUser,]
    # renderer_classes = [JSONRenderer]

    def post(self, request):
        respon = {'message': 'success', 'data': {}, 'code': 10000}
        if not request.user.is_anonymous:
            print(request.POST)
            respon['data']['user'] = request.user.username
            to_userid = request.POST.get('user2', None)
            content = request.POST.get('article', '暂未填写内容')
            # parent_id = request.POST.get('parent_id', '')
            root_id = request.POST.get('root', None)
            image = request.POST.get('image', None)
            msg_obj = Message()
            if root_id:
                root = Message.objects.filter(id=root_id).first()
                msg_obj.root = root
            # if parent_id:
            #     parent = Message.objects.filter(id=parent_id).first()
            #     Message.parent = parent
            if to_userid:
                to_user = User.objects.filter(id=to_userid).first()
                print(to_user)
                msg_obj.user2 = to_user
            if image:
                msg_obj.image = image
            msg_obj.content = content
            msg_obj.user1 = request.user
            msg_obj.save()
            tree = MsgTree().get_msgtree(self)
            if tree:
                respon['data']['one'] = tree
        else:
            return redirect('/u/login/')
        return redirect('/m/gbook')

    def get(self, request):
        respon = {'message': 'success', 'data': {}, 'code': 10000}
        if request.user.is_anonymous:
            respon['data']['user'] = None
        else:
            respon['data']['user'] = request.user.username
        tree = MsgTree().get_msgtree(self)
        if tree:
            respon['data']['one'] = tree
            print(len(respon['data']['one']))
            # respon['data']['two'] = tree[1]
        # return Response(respon)
        return Response(respon, template_name='gbook.html')