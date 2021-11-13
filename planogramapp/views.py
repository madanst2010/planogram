from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from planogramapp.models import Planogram, PlanogramDetails
from planogramapp.serializer import PlanogramDetailSerializer, PlanogramSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
import json
from django.core import serializers
# Create your views here.
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def planogram_add(req):
    if req.method == "POST":
        json_data = req.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
       
        python_data1 = {}
        python_data1['name'] = python_data['name']
        python_data.pop('name')
        serializer = PlanogramSerializer(data = python_data1)
        if serializer.is_valid():
            obj = Planogram.objects.create(**python_data1)
            if obj is not None:
                python_data['plano_id'] = {'plano_id' : '1'}
                print(obj.id)
                newId = obj.id
                newArr = python_data['value']
                ok = True
                for i in newArr:
                    i['plano_id'] = newId
                    print('this is i')
                    print(i)
                    print(type(i))
                    serializer = PlanogramDetailSerializer(data = i)
                    print(serializer.is_valid(), serializer.errors)
                    if serializer.is_valid():
                        print("okkkkkkkk")
                        serializer.save()
                res = {'msg': 'data posted successfully'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type = 'application/json')
            return HttpResponse({"something wrong"},status=500)
        return HttpResponse({"something wrong"},status=500)
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def planogram_get(req):
    if req.method == "GET":
        obj = Planogram.objects.all()
        ans = []
        for i in obj.iterator():
            data = PlanogramDetails.objects.filter(plano_id_id = i.id)
            data = serializers.serialize('json', data)
            ans.append({"name" : i.name, "value" : data})
        res = {'msg': 'data posted successfully'}
        json_data = JSONRenderer().render(res)
        ans = json.dumps(ans)
        print(type(ans))
        return HttpResponse(ans, content_type = 'application/json')
    return HttpResponse({"something wrong"},status=500)