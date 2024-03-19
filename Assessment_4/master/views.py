from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import todoApiModel
from .serializer import todoApiModelSerializer


@api_view(['GET','POST'])
def todoListAPI(request):
    if request.method=="GET":
        query = todoApiModel.objects.all()
        serializer = todoApiModelSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=="POST":
        query = request.data
        serializer = todoApiModelSerializer(data=query)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PATCH','PUT',"DELETE"])
def todoDetailsAPI(request,id):
    query = todoApiModel.objects.get(id=id)
    if request.method=="GET":
        serializer = todoApiModelSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=="PUT":
        serializer = todoApiModelSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="PATCH":
        serializer = todoApiModelSerializer(query,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        query.delete()
        return Response("Data Deleted Successfully",status=status.HTTP_204_NO_CONTENT)
