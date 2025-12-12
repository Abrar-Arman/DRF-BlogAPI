from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class BaseCreateView(generics.CreateAPIView):
    msg="Created successfully"
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": self.msg},
            status=status.HTTP_201_CREATED
        )