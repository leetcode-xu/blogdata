from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
# Create your views here.
from rest_framework.views import APIView

from .models import *
from .forms import *
# class AuthUser():

class AuthPassword(BaseAuthentication):
    def authenticate(self, request):
        pass


# url: /u/login/
class Login(APIView):
    authentication_classes = [SessionAuthentication, ]
    # renderer_classes = [CustomBrowsableAPIRenderer,]
    template = 'login.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('/')
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # print('post'*20)
        # sessionid = request.COOKIES['sessionid']
        # print(request.session.has_key(sessionid))
        # print('post'*20)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, password)
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            auth.login(request, user)
            print(request.user, 'request.user')
            return redirect('/')
            # print('ok')
            # return HttpResponse('登录成功')
        else:
            # print('shibai')
            return redirect('/u/login/')


# url: /u/register/
class RegisterView(APIView):
    # renderer_classes = [JSONRenderer,]
    def get(self, request):
        if request.user.is_anonymous:
            return Response(template_name='register.html')
        else:
            return redirect('/')

    def post(self, request):
        respon = {'message': 'success', 'data': '', 'code': 10000}
        username = request.POST.get('username', '')
        if Verify_regis(request.POST).is_valid():
            try:
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                email = request.POST.get('email', '')
                user_obj = User(username=username, password=make_password(password), email=email)
                user_obj.save()
                auth.login(request, user_obj)
                return redirect('/')
            except Exception as e:
                respon['message'] = str(e)
                respon['code'] = 10001
        else:
            respon['message'] = Verify_regis(request.POST).errors
            respon['code'] = 10002
        return Response(respon, template_name='register.html')


# url: /u/logout/
class LogoutView(APIView):
    def get(self, request):
        try:
            status = auth.logout(request)
            print(status)
        except Exception as e:
            pass
        return redirect('/')


# url: /u/info/
class InfoView(APIView):
    def get(self, request):
        return Response(template_name='info.html')