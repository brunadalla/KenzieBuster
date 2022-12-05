from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status
from users.serializers import UserSerializer

class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


