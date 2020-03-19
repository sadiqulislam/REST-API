from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers, UserSerializers
from .models import Tasks
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# from rest_framework import filters
# from django.db.models.query import QuerySet


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tasks.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers
    # filter_backends = filters.SearchFilter
    # filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    # filter_fields = ('completed',)
    # ordering = ('-date_created',)
    # search_field = ('task_name',)


class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers