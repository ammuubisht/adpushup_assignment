import csv
from base.models import AdvertData

with open('data_file.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        AdvertData.objects.create(date=row[0],
        key_values=row[1][row.find("=")+1:],
        country = row[2],
        key_value_id = row[3],
        country_id = row[4],
        total_code_served_count = row[5],
        unfilled_impressions = row[6],
        total_impresions = row[7],
        cpm_cpc_revenue = row[8],
        average_ecpm = row[9],
        ad_server_impressions = row[10],
        ad_server_average_ecpm = row[11],
        ad_sever_cpm_cpc_revenue = row[12],
        ad_exchange_impressions = row[13],
        ad_exchange_revenue = row[14],
        ad_exchange_average_ecpm = row[15]
        )
    