from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.


class CalculatorView(viewsets.ViewSet):

    @staticmethod
    def add_one_to_number(request):
        number = request.data.get('number')
        return Response({"result": number + 1})

    @staticmethod
    def add_two_to_number(request):
        number = request.data.get('number')
        return Response({"result": number + 2})
