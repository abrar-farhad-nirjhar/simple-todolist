from rest_framework import viewsets


from .serializers import *

from .models import *

from rest_framework.permissions import IsAuthenticated


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer




class TaskViewset(viewsets.ModelViewSet):

    queryset = Task.objects.all()

    permission_classes = (IsAuthenticated,)

    serializer_class = TaskSerializer

    def get_queryset(self):

        return Task.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):

        data = request.data

        t = Task()
        t.task = data['task']
        t.user = request.user

        t.save()
        return t


