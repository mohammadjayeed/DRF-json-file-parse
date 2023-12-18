from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from .serializers import AccountabilitySerializer
from .models import Accountability


class FileUpload(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=json):
       

       file = request.data['file']
       data = json.load(file)
       jtopy=json.dumps(data) 
       dict_json=json.loads(jtopy)
    #    print(type(dict_json))
    #    print(dict_json[0]['alert_type'])

       from datetime import datetime

       for item in dict_json:
          timestamp = item['timestamp']
          alert_type = item['alert_type']
          
        #   print(timestamp)
        #   print(alert_type)
          
          dt_obj = datetime.fromtimestamp(timestamp/1000)
          
          print("date:",dt_obj)
          body = {
              
            'date': dt_obj,
            'alert': alert_type

          }
          serializer = AccountabilitySerializer(data=body)
          serializer.is_valid(raise_exception=True)
          serializer.save()


       return Response('ok')
    def get(self,request):
        return Response('ok')