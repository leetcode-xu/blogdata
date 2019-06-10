from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.response import Response

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


class GbookView(APIView):
    # authentication_classes = [AuthUser,]

    def post(self, request):
        respon = {'message': 'success', 'data': {}, 'code': 10000}
        if not request.user.is_anonymous:
            to_userid = request.POST.get('id', '')
            to_user = User.objects.filter(id=to_userid).first()
            content = request.POST.get('content', '')
            to_msg_id = request.POST.get('to_msg_id', '')
            msg_obj = Message()
            msg_obj.content = content
            msg_obj.to_msg_id = to_msg_id
            msg_obj.save()
            msg_obj.users.add(request.user, to_user)
        else:
            return redirect('/u/login/')
        return redirect('/m/gbook/')

    def get(self, request):
        return Response(template_name='gbook.html')