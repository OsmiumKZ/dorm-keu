from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from . import serializers, models
from django.db.models import Q
from django.core.serializers import serialize
import requests


def create_account(answer, educational_f, login, password):
    mother = models.Parent.objects.create(
        name_f=answer.validated_data['parent_mother']['name_f'],
        name_l=answer.validated_data['parent_mother']['name_l'],
        patronymic=answer.validated_data['parent_mother']['patronymic'],
        phone=answer.validated_data['parent_mother']['phone']
    )
    father = models.Parent.objects.create(
        name_f=answer.validated_data['parent_father']['name_f'],
        name_l=answer.validated_data['parent_father']['name_l'],
        patronymic=answer.validated_data['parent_father']['patronymic'],
        phone=answer.validated_data['parent_father']['phone']
    )
    account = models.Account.objects.create(
        login=login,
        password=password,
        student_id=answer.validated_data['id'],
        name_f=answer.validated_data['name_f'],
        name_l=answer.validated_data['name_l'],
        patronymic=answer.validated_data['patronymic'],
        gender_id=answer.validated_data['gender_id'],
        educational_form=educational_f,
        citizenship=answer.validated_data['citizenship'],
        uin=answer.validated_data['uin'],
        address=answer.validated_data['address'],
        city=answer.validated_data['city'],
        country=answer.validated_data['country'],
        phone=answer.validated_data['phone'],
        email=answer.validated_data['email'],
        privileges=answer.validated_data['privileges'],
        group=answer.validated_data['group'],
        parent_mother=mother,
        parent_father=father
    )
    return serializers.AccountSerializer(account).data


def update_parent(answer, id, type_parent):
    try:
        parent = models.Parent.objects.get(pk=id)
        parent.name_f = answer.validated_data[type_parent]['name_f']
        parent.name_l = answer.validated_data[type_parent]['name_l']
        parent.patronymic = answer.validated_data[type_parent]['patronymic']
        parent.phone = answer.validated_data[type_parent]['phone']
        parent.save()
    except models.Parent.DoesNotExist:
        pass


def account_to_json(login, password):
    account = models.Account.objects.get(
        Q(login=login),
        Q(password=password)
    )
    return serializers.AccountSerializer(account).data


def update_account(answer, account, educational_f, login, password):
    if account.parent_mother_id:
        update_parent(answer, account.parent_mother_id, 'parent_mother')

    if account.parent_father_id:
        update_parent(answer, account.parent_father_id, 'parent_father')

    account.login = login
    account.password = password
    account.student_id = answer.validated_data['id']
    account.name_f = answer.validated_data['name_f']
    account.name_l = answer.validated_data['name_l']
    account.patronymic = answer.validated_data['patronymic']
    account.gender_id = answer.validated_data['gender_id']
    account.educational_form = educational_f
    account.citizenship = answer.validated_data['citizenship']
    account.uin = answer.validated_data['uin']
    account.address = answer.validated_data['address']
    account.city = answer.validated_data['city']
    account.country = answer.validated_data['country']
    account.phone = answer.validated_data['phone']
    account.email = answer.validated_data['email']
    account.privileges = answer.validated_data['privileges']
    account.group = answer.validated_data['group']
    account.save()
    return account_to_json(login, password)


@api_view(['POST'])
@permission_classes((AllowAny,))
def auth_account(request):
    body = serializers.AuthAccountSerializer(data=request.data)
    if body.is_valid():
        body.validated_data['password']
        response = requests.post(
            'http://127.0.0.1:8001/api/auth/',
            data={
                'login': body.validated_data['login'],
                'password': body.validated_data['password']
            }
        )
        if response.status_code == 200:
            answer = serializers.ParseAccountSerializer(data=response.json())
            if answer.is_valid():
                try:
                    educational_form = models.EducationalForm.objects.get(
                        pk=answer.validated_data['educational_form'])
                    try:
                        account = models.Account.objects.get(
                            Q(login=body.validated_data['login']),
                            Q(password=body.validated_data['password'])
                        )
                        return Response(
                            update_account(
                                answer,
                                account,
                                educational_form,
                                body.validated_data['login'],
                                body.validated_data['password']
                            )
                        )
                    except models.Account.DoesNotExist:
                        return Response(
                            create_account(
                                answer,
                                educational_form,
                                body.validated_data['login'],
                                body.validated_data['password']
                            )
                        )
                except models.EducationalForm.DoesNotExist:
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_409_CONFLICT)


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
    if request.headers.get('Educationalform') != None:
        report_list = models.Report.objects.filter(account__educational_form__id=request.headers.get('Educationalform'))
    elif request.headers.get('Gender') != None:
        report_list = models.Report.objects.filter(account__gender__id=request.headers.get('Gender'))
    elif request.headers.get('Children') != None:
        report_list = models.Report.objects.order_by('account__children').reverse()
    elif request.headers.get('Datecreate') != None:
        report_list = models.Report.objects.order_by('date_create').reverse()
    elif request.headers.get('Dateupdate') != None:
        report_list = models.Report.objects.order_by('date_update').reverse()
    elif request.headers.get('All') != None:
        report_list = models.Report.objects.all()
    else:
        report_list = models.Report.objects.filter(active=0)
    return Response(serializers.ReportSerializer(report_list, many=True).data)
    

@api_view(['GET'])
@permission_classes((AllowAny,))
def requests_sort(request):
    """Метод выводит сортированные заявления."""
    if request.headers.get('Educationalform') != None:
        request_list = models.Request.objects.filter(account__educational_form__id=request.headers.get('Educationalform'))
    elif request.headers.get('Gender') != None:
        request_list = models.Request.objects.filter(account__gender__id=request.headers.get('Gender'))
    elif request.headers.get('Children') != None:
        request_list = models.Request.objects.order_by('account__children').reverse()
    elif request.headers.get('Datecreate') != None:
        request_list = models.Request.objects.order_by('date_create').reverse()
    elif request.headers.get('Dateupdate') != None:
        request_list = models.Request.objects.order_by('date_update').reverse()
    elif request.headers.get('All') != None:
        request_list = models.Request.objects.all()
    else:
        request_list = models.Request.objects.filter(active=0)
    return Response(serializers.RequestSerializer(request_list, many=True).data)