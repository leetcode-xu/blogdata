from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import *
from rest_framework.renderers import JSONRenderer

import csv
# Create your views here.


class TopicSerializer(ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Topic
        depth = 2
        fields = '__all__'


class ReplySer(ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Reply
        depth = 2
        fields = "__all__"


class PageTopic(PageNumberPagination):
    page_size = 21
    max_page_size = 21
    page_query_param = 'page'
    page_size_query_param = 'size'
    ordering = 'read_num'


class IndexView(APIView):
    # renderer_classes = [JSONRenderer,]

    def get(self, request):
        respon = {'message': 'success', 'data': {}, 'code':10000}
        if request.user.is_anonymous:
            respon['data']['user'] = None
        else:
            respon['data']['user'] = request.user.username
        topic = Topic.objects.all().order_by('id')
        page_list = PageTopic().paginate_queryset(topic, self.request, view=self)
        topic_ser = TopicSerializer(instance=page_list, many=True)
        respon['data'].update({'topic_title': topic_ser.data[:3]})
        respon['data'].update({'topic_left': topic_ser.data[3:5]})
        respon['data'].update({'topic_tebie': topic_ser.data[5:8]})
        respon['data'].update({'topic_body': topic_ser.data[8:21]})
        return Response(respon, template_name='index.html')


class AddTopic(APIView):
    renderer_classes = [JSONRenderer]

    # def get(self, request):
    #     s = 'static/images/aiqing/爱情.csv'
    #     data = csv.reader(open(s, 'r', encoding='utf8'))
    #     try:
    #         for index, line in enumerate(data):
    #             lists = ''.join(line).split('#')
    #             if not lists[1]:
    #                 break
    #             topic_obj = Topic()
    #             topic_obj.title = lists[0]
    #             topic_obj.content = lists[1]
    #             topic_obj.image = 'static/images/aiqing/' + lists[2]
    #             topic_obj.tag = 4
    #             topic_obj.save()
    #             print('第%s行写入数据库成功' % index)
    #     except Exception as e:
    #         import datetime
    #         print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e)
    #     # topic_obj = Topic.objects.all().last()
    #     # print([topic_obj.title, topic_obj.content, topic_obj.image, topic_obj.tag])
    #     # return Response([topic_obj.title, topic_obj.content, topic_obj.image, topic_obj.tag])
    #     return Response('OK')


class Reply_Topic:

    def __init__(self, topic_id):
        reply_obj = Reply.objects.filter(topic=topic_id).all()
        reply_ser = ReplySer(instance=reply_obj, many=True)
        self.reply_ser = sorted(reply_ser.data, key=lambda x: x['time'])
        self.reply_one = []
        reply_two = []
        for i in self.reply_ser:
            if len(i.get('users', [])) == 1:
                self.reply_one.append(i)
            else:
                reply_two.append(i)
        for one in self.reply_one:
            one['two'] = []
            for two in reply_two:
                if one['users'][0] in two['users']:
                    one['two'].append(two)
                    reply_two.remove(two)


class TopicInfo(APIView):
    # renderer_classes = [JSONRenderer]
    def get(self, request):
        respon = {'message': 'success', 'data': {}, 'code': 10000}
        try:
            id = request.GET.get('id', 100)
            topic_obj = Topic.objects.get(id=id)
            topic_obj.read_num += 1
            topic_obj.save()
            ts = TopicSerializer(instance=topic_obj, many=False)
            if request.user.is_anonymous:
                respon['data']['user'] = False
            else:
                respon['data']['user'] = request.user.username
            respon['data']['topic'] = ts.data
            last_obj = Topic.objects.filter(id=int(id)-1).first()
            if last_obj:
                last_obj = TopicSerializer(instance=last_obj, many=False)
                respon['data']['last'] = last_obj.data
            else:
                respon['data']['last'] = ts.data
            next_obj = Topic.objects.filter(id=int(id)+1).first()
            if next_obj:
                next_obj = TopicSerializer(instance=next_obj, many=False)
                respon['data']['next'] = next_obj.data
            else:
                respon['data']['next'] = ts.data
            obj = Reply_Topic(int(id))
            respon['data']['one'], respon['data']['num'] = obj.reply_one, len(obj.reply_ser)
            topics = Topic.objects.all().order_by('read_num')
            topics = PageTopic().paginate_queryset(topics, request, view=self)
            topics = TopicSerializer(instance=topics, many=True)
            respon['data']['dianji0'] = topics.data[0]
            respon['data']['dianji'] = topics.data[1:5]
            respon['data']['tuijian0'] = topics.data[5]
            respon['data']['tuijian'] = topics.data[6:10]
            respon['data']['tebie'] = topics.data[10:13]
        except Exception as e:
            respon['message'] = 'fail'
            respon['data']['error'] = str(e)
            respon['code'] = 10013
        # return Response(respon)
        return Response(respon, template_name='info.html')


class ReplyAdd(APIView):
    # renderer_classes = [JSONRenderer, ]

    def post(self, request):
        respon = {'message': 'success', 'data': {}, 'code': 10000}
        if request.user.is_anonymous:
            return redirect('/u/login/')
        try:
            topic_id = request.POST.get('topic_id', '')
            topic_obj = Topic.objects.get(id=topic_id)
            message = request.POST.get('article', '')
            user_two = message.split()[0]
            print(user_two,'sdf'*7)
            if user_two[0] == '@':
                user_two = User.objects.filter(username=user_two[1:]).first()
                print(user_two.username)
            else:
                user_two = None
            reply_obj = Reply()
            reply_obj.message = ' '.join(message.split()[1:])
            reply_obj.topic = topic_obj
            reply_obj.save()
            reply_obj.users.add(request.user)
            if user_two:
                reply_obj.users.add(user_two)
        except Exception as e:
            respon['message'] = 'fail'
            respon['data']['error'] = str(e)
            respon['code'] = 10014
        return redirect('/topicinfo/?id=%s'%topic_id)

class AixinView(APIView):
    renderer_classes = [JSONRenderer,]

    def post(self, request):
        respon = {'message': 'fail', 'data': {}, 'code': 10015}
        id = request.POST.get('id', '')
        if id:
            topic_obj = Topic.objects.filter(id=id).first()
            if topic_obj:
                topic_obj.aixin += 1
                topic_obj.save()
                respon['message'] = 'success'
                respon['data']['aixin'] = topic_obj.aixin
                respon['code'] = 10000
        return Response(respon)


class FenleiView(APIView):

    def get(self,request):
        return Response(template_name='list.html')


class CeShi(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        return Response(Reply_Topic(12).reply_one)