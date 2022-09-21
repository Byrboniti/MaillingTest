from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from .models import Mailing, Client, Text_message
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class Text_MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Text_message.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        queryset_mailing = Mailing.objects.all()
        get_object_or_404(queryset_mailing, pk=pk)
        queryset = Text_message.objects.filter(mailing_id=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullinfo(self, request):
        total_count = Mailing.objects.count()
        mailing = Mailing.objects.values('id')
        content = {'All mailings': total_count,
                   'The number of messages sent': ''}
        result = {}

        for row in mailing:
            res = {'all': 0, 'ok': 0, 'Not ok': 0}
            mail = Text_message.objects.filter(mailing_id=row['id']).all()
            group_sent = mail.filter(sending_status='ok').count()
            group_no_sent = mail.filter(sending_status='Not ok').count()
            res['all'] = len(mail)
            res['ok'] = group_sent
            res['Not ok'] = group_no_sent
            result[row['id']] = res

        content['The number of messages sent'] = result
        return Response(content)