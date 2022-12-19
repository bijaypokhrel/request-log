from django.shortcuts import render
from .models import RequestLog
from rest_framework.response import Response
from .serializers import RequestLogSerializer
from rest_framework import status
from rest_framework.views import APIView
import requests
import datetime


def convert(date_time):
    format = '%a, %d %b %Y %H:%M:%S %Z'
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str


response = requests.get('https://google.com/')
created_at = convert(response.headers['Date'])
response_at = convert(response.headers['Date'])
url = response.url
request_headers = response.headers['Content-type']
request_textfield = response.headers['Content-type']
response_code = response.status_code
response_headers = response.headers['Content-type']
response = response.text


data = {
    'created_at': created_at,
    'response_at': response_at,
    'sec_response_time': 1,
    'url': url,
    'request_headers': request_headers,
    'request_textfield': request_textfield,
    'response_code': response_code,
    'response_headers': response_headers,
    'response': response
}
serializer = RequestLogSerializer(data=data)
if serializer.is_valid():
    serializer.save()


class RequestLogAPI(APIView):
    def get(self, request, format=None):
        re = RequestLog.objects.all()
        serializer = RequestLogSerializer(re, many=True)
        return Response(serializer.data)
