from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .models import UserType
from .serializers import UserTypeSerializer


class RetrieveUpdateDeleteUserType(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
    ):

    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ListCreateUserType(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
    ):

    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
