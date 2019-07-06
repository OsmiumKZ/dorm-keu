from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from . import serializers, models, utils, constructor_docx
from django.db.models import Q
from django.http import FileResponse
import os
import requests


@api_view(['POST'])
@permission_classes((AllowAny,))
def auth_account(request):
    return utils.handler_auth_account(request)


class ReportsViewAPI(generics.ListCreateAPIView):
    """Класс позволяет создавать и получать экземпляры отчёты."""
    serializer_class = serializers.ReportSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return models.Report.objects.filter(active=0)


class RequestsViewAPI(generics.ListCreateAPIView):
    """Класс позволяет создавать и получать экземпляры заявления."""
    serializer_class = serializers.RequestSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return models.Request.objects.filter(active=0)


class ReportViewAPI(generics.RetrieveUpdateDestroyAPIView):
    """Класс позволяет удалять, изменять и получать экземпляр отчёта."""
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = (AllowAny,)


class RequestViewAPI(generics.RetrieveUpdateDestroyAPIView):
    """Класс позволяет удалять, изменять и получать экземпляр заявления."""
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer
    permission_classes = (AllowAny,)


@api_view(['GET'])
@permission_classes((AllowAny,))
def reports_sort(request):
    """Метод выводит сортированные отчёты."""
    return Response(
        serializers.RequestSerializer(
            utils.get_sort_data(models.Report.objects, request),
            many=True
        ).data
    )


@api_view(['GET'])
@permission_classes((AllowAny,))
def requests_sort(request):
    """Метод выводит сортированные заявления."""
    return Response(
        serializers.RequestSerializer(
            utils.get_sort_data(models.Request.objects, request),
            many=True
        ).data
    )


@api_view(['GET'])
@permission_classes((AllowAny,))
def db_base(request):
    return Response(utils.get_db)


@api_view(['GET'])
@permission_classes((AllowAny,))
def statistic(request):
    return Response(utils.get_statistic())


@api_view(['GET'])
@permission_classes((AllowAny,))
def rooms_floor(request, pk):
    return Response(utils.get_rooms_floor(pk))


def send_direction_file(response, pk):
    """Отправить файл направление."""
    try:
        direction = models.Report.objects.get(pk=pk)
        name_file = constructor_docx.direction(
            name_f=direction.account.name_f, 
            name_l=direction.account.name_l, 
            dorm=direction.room.floor.dorm.id, 
            address=direction.account.address, 
            phone=direction.account.phone, 
            patronymic=direction.account.patronymic
        )

        response = FileResponse(open(name_file, 'rb'))
        os.remove(name_file)

        return response
    except models.Report.DoesNotExist:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def send_request_file(response, pk):
    """Отправить файл заявление."""
    try:
        request = models.Request.objects.get(pk=pk)
        name_file = constructor_docx.request(
            dorm=request.room.floor.dorm.id, 
            date=request.date_update, 
            number_request=request.id, 
            gender=request.account.gender.id, 
            address=request.account.address, 
            name_f=request.account.name_f, 
            name_l=request.account.name_l, 
            phone=request.account.phone, 
            group=request.account.group, 
            children=request.account.children, 
            patronymic=request.account.patronymic
        )

        response = FileResponse(open(name_file, 'rb'))
        os.remove(name_file)

        return response
    except models.Request.DoesNotExist:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)