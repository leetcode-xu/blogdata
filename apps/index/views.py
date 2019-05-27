from django.shortcuts import render, HttpResponse
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
        topic = Topic.objects.all()
        page_list = PageTopic().paginate_queryset(topic, self.request, view=self)
        topic_ser = TopicSerializer(instance=page_list, many=True)
        respon['data'].update({'topic_title': topic_ser.data[:3]})
        respon['data'].update({'topic_left': topic_ser.data[3:5]})
        respon['data'].update({'topic_tebie': topic_ser.data[5:8]})
        respon['data'].update({'topic_body': topic_ser.data[8:21]})
        return Response(respon, template_name='index.html')


class AddTopic(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        s = 'static/images/aiqing/爱情.csv'
        data = csv.reader(open(s, 'r', encoding='utf8'))
        try:
            for index, line in enumerate(data):
                lists = ''.join(line).split('#')
                if not lists[1]:
                    break
                topic_obj = Topic()
                topic_obj.title = lists[0]
                topic_obj.content = lists[1]
                topic_obj.image = 'static/images/aiqing/' + lists[2]
                topic_obj.tag = 4
                topic_obj.save()
                print('第%s行写入数据库成功' % index)
        except Exception as e:
            import datetime
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e)
        # topic_obj = Topic.objects.all().last()
        # print([topic_obj.title, topic_obj.content, topic_obj.image, topic_obj.tag])
        # return Response([topic_obj.title, topic_obj.content, topic_obj.image, topic_obj.tag])
        return Response('OK')
