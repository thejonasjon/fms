from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form, Response as FormResponse
from .serializers import FormSerializer, ResponseSerializer


class FormList(APIView):
    """Views for the Form APIs."""

    def get(self, request):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormDetail(APIView):
    """DetailViews for the Form APIs."""

    def get(self, request, pk):
        try:
            form = Form.objects.get(id=pk)
            serializer = FormSerializer(form)
            return Response(serializer.data)
        except Form.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            form = Form.objects.get(id=pk)
            serializer = FormSerializer(form, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Form.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            form = Form.objects.get(id=pk)
            form.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Form.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ResponseList(APIView):
    """Views for the Response APIs."""

    def get(self, request):
        responses = FormResponse.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponseDetail(APIView):
    """DetailViews for the Response APIs."""

    def get(self, request, pk):
        try:
            response = FormResponse.objects.get(id=pk)
            serializer = ResponseSerializer(response)
            return Response(serializer.data)
        except FormResponse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            response = FormResponse.objects.get(id=pk)
            serializer = ResponseSerializer(response, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FormResponse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            response = FormResponse.objects.get(id=pk)
            response.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FormResponse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
