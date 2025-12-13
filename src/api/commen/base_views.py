from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async

class BaseCreateView:
    msg = "Created successfully"

    async def perform_create(self, serializer):
        await sync_to_async(serializer.save)()

    async def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        await self.perform_create(serializer)

        return Response(
            {"message": self.msg},
            status=status.HTTP_201_CREATED
        )