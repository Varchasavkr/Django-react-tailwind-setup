from django.shortcuts import render ,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
def index(request):
    return HttpResponse("jai shree ram")

# Create your views here.
