# import viewsets
from rest_framework import viewsets
# import local data
from .serializers import UserSerializer
from .models import UserModel
# create a viewse
class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = UserModel.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer