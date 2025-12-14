from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async
async def get_data(serializer):
    """Use adata if the serializer supports it, data otherwise."""
    return (
        await serializer.adata
        if hasattr(serializer, "adata")
        else await sync_to_async(lambda: serializer.data)()
    )

class BaseCreateView:
    msg = "Created successfully"

    async def perform_acreate(self, serializer):
        await serializer.asave()

    async def acreate(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      await sync_to_async(serializer.is_valid)(raise_exception=True)
      await self.perform_acreate(serializer)
      data = await get_data(serializer)
      return Response(
            {"message": self.msg},
            status=status.HTTP_201_CREATED
        )