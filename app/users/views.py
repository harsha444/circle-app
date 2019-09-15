from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from users import serializers
from users import models


# class UserView(APIView):
#     serializer_class = serializers.UserProfileSerializer
#
#     def get(self, request, format=None):
#         """Get UserProfile"""
#         pass
#
#     def post(self, request, format=None):
#         """Create UserProfile"""
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             name = serializer.get_validated_data.get('name')
#             return Response({'message': name})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and retrieving UserProfile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
