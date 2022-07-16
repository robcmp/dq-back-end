from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client, Company
from .serializers import ClientSerializer, CompanySerializer


class ClientAPIView(APIView):
    serializer_class = ClientSerializer

    def getClientIds(self):
        clients = Client.objects.all()
        return clients

    def get(self, request, *args, **kwargs):
        clients = self.getClientIds()
        serializers = ClientSerializer(clients, many=True)

        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        client_data = request.data

        new_client = Client.objects.create(
            nin=client_data["nin"], first_name=client_data["first_name"], last_name=client_data["last_name"])

        new_client.save()

        serializer = ClientSerializer(new_client)

        return Response(serializer.data)


class CompanyAPIView(APIView):
    serializer_class = CompanySerializer

    def getCompanies(self):
        companies = Company.objects.all()
        return companies

    def get(self, request, *args, **kwargs):
        companies = self.getCompanies()
        serializers = CompanySerializer(companies, many=True)

        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        company_data = request.data

        new_company = Company.objects.create(name=company_data["name"])

        new_company.save()

        serializer = CompanySerializer(new_company)

        return Response(serializer.data)
