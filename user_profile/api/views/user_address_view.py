from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from user_profile.api.models.user_address_model import Province, UserAddress
from user_profile.api.serializers.user_address_serializer import UserAddressSerializer, ProvinceSerializer


class ProvinceView(viewsets.ViewSet):
    """province view"""
    queryset = Province.objects.all()

    def list(self, request):
        serializer = ProvinceSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        province = get_object_or_404(self.queryset, pk=pk)
        serializer = ProvinceSerializer(province)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        province = get_object_or_404(self.queryset, pk=pk)
        serializer = ProvinceSerializer(province, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        province = get_object_or_404(self.queryset, pk=pk)
        serializer = ProvinceSerializer(province, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        province = get_object_or_404(self.queryset, pk=pk)
        province.delete()
        return Response({"message": "Province deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    

class UserAddressView(viewsets.ViewSet):
    """User address veiw"""
    queryset = UserAddress.objects.all()

    def list(self, request):
        serializer = UserAddressSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        address = get_object_or_404(self.queryset, pk=pk)
        serializer = UserAddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        address = get_object_or_404(self.queryset, pk=pk)
        serializer = UserAddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        address = get_object_or_404(self.queryset, pk=pk)
        address.delete()
        return Response({"message": "Address deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    
    def get_user_address_with_user_id(self, request, user_id=None):
        """get user address with user_id"""
        serializer = UserAddressSerializer(self.queryset, user=user_id) 
        return Response(serializer.data, status=status.HTTP_200_OK)