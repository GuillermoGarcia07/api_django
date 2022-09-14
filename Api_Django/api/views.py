from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import alumnos

# Create your views here.

class alumnosView(View):
    
    def get(self, request):
        l = list(alumnos.objects.values())
        if len(l) > 0:
            datos = {'messages' : 'Success', 'alumnos' : l}
        else:
            datos = {'messages' : 'No Hay Alumnos'}  
        return JsonResponse(datos)

    def put(self, request):
        alumnos = alumnos(request.POST)
        if alumnos.is_valid():
            alumnos.save()
            datos = {'messages' : 'Success'}
        return JsonResponse(datos)

              
    def delete(self, request):
        pass
    