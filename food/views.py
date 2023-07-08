from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Food
from .serializers import FoodSerializer


class FoodListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the Food items for given requested user
        """
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the Food with given Food data
        """
        data = {
            'name': request.data.get('name'),
            'carbs': request.data.get('carbs'),
            'user': request.user.id
        }
        serializer = FoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodDetailApiView(APIView):

    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, food_id):
        """
        Helper method to get the object with given food_id
        """
        try:
            return Food.objects.get(id=food_id)
        except Food.DoesNotExist:
            return None

    def get(self, request, food_id, *args, **kwargs):
        '''
        Retrieves the food with given food_id
        '''
        food_instance = self.get_object(food_id)
        if not food_instance:
            return Response(
                {"res": "Object with food id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FoodSerializer(food_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, food_id, *args, **kwargs):
        """
        Updates the food item with given food_id if exists
        """
        food_instance = self.get_object(food_id)
        if not food_instance:
            return Response(
                {"res": "Object with food id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name', food_instance.name),
            'carbs': request.data.get('carbs', food_instance.carbs),
            'user': request.user.id
        }
        serializer = FoodSerializer(instance=food_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, food_id, *args, **kwargs):
        """
        Deletes the food item with given food_id if exists
        """
        food_instance = self.get_object(food_id)
        if not food_instance:
            return Response(
                {"res": "Object with food id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        food_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
