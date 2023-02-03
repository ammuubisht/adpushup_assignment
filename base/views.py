from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import AdvertData
import csv
import matplotlib.pyplot as plt
from .serializers import AdvertDataSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .utils import get_plot
import datetime



class Dashboard(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/index.html'
    all_country_query = AdvertData.objects.all()


    def get(self, request, **kwargs):

        
        if request.GET.get('country'):
            
            countries_query_list = []
            for country in request.GET.getlist('country'):
                queryset = AdvertData.objects.get(country=country.title(), key_values=request.GET.get('key-value'), date=request.GET.get('date'))
                countries_query_list.append(queryset)
            
            x_values = []
            y_values = []
            for val in countries_query_list:
                
                x_value_query = val.__getattribute__((request.GET.get('x-value')))
                x_values.append(x_value_query)
                y_value_query = val.__getattribute__((request.GET.get('y-value')))
                y_values.append(y_value_query)

            
            plot = get_plot(x_values, y_values, (request.GET.get('x-value')), (request.GET.get('y-value')), countries_query_list)
        else:
            plot = None

        return Response({'data': plot, 'countries': self.all_country_query})


class FetchData(APIView):
    serializer = AdvertDataSerializer

    def get(self, request, **kwargs):
        query = AdvertData.objects.all()
        serializer = self.serializer(query, many=True)

        return Response({'data': serializer.data})


# Function to add data to database

# def data_entry(request):
#     with open('data_file.csv') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader: 
#             AdvertData.objects.update_or_create(date=row[0],
#             key_values=row[1][row[1].find("=")+1:],
#             country = row[2],
#             key_value_id = row[3],
#             country_id = row[4],
#             total_code_served_count = row[5],
#             unfilled_impressions = row[6],
#             total_impresions = row[7],
#             cpm_cpc_revenue = row[8],
#             average_ecpm = row[9],
#             ad_server_impressions = row[10],
#             ad_server_average_ecpm = row[11],
#             ad_sever_cpm_cpc_revenue = row[12],
#             ad_exchange_impressions = row[13],
#             ad_exchange_revenue = row[14],
#             ad_exchange_average_ecpm = row[15]
#             )
    
#     return HttpResponse('Data Added Successfully')