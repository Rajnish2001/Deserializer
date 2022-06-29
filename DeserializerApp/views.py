from django.http import HttpResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        json_data = request.body  #Json data throught the body
        stream = io.BytesIO(json_data) #changeing jsondata into binary data
        pythondata = JSONParser().parse(stream) #changing binary data into Python Native Data
        serializer = StudentSerializer(data=pythondata) #changing Python Native Data into Complex Data

        if serializer.is_valid():   #Chack validation and if data is valid than save data
            serializer.save()
            res = {'msg':'Your data is Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors) #If any errors in your json data than follow this process
        return HttpResponse(json_data,content_type='application/json')
        