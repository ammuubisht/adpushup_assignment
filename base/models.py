from django.db import models

# Create your models here.

class AdvertData(models.Model):
    choices = (
        ('control', 'control'),
        ('experiment', 'experiment')
    )

    date = models.DateField(("Date"))
    key_values = models.CharField(("Key-values"), max_length = 20, choices=choices, default=1)
    country = models.CharField(("Country"),max_length=50)
    key_value_id = models.BigIntegerField(("Key-values ID"))
    country_id = models.IntegerField(("Country ID"))
    total_code_served_count = models.IntegerField(("Total code served count"))
    unfilled_impressions = models.IntegerField(("Unfilled impressions"))
    total_impresions = models.IntegerField(("Total impressions"))
    cpm_cpc_revenue = models.FloatField(("Total CPM and CPC revenue ($)"))
    average_ecpm = models.FloatField(("Total average eCPM ($)"))
    ad_server_impressions = models.IntegerField(("Ad server impressions"))
    ad_server_average_ecpm = models.FloatField(("Ad server average eCPM ($)"))
    ad_sever_cpm_cpc_revenue = models.FloatField(("Ad server CPM and CPC revenue ($)"))
    ad_exchange_impressions = models.IntegerField(("Ad Exchange impressions"))
    ad_exchange_revenue = models.FloatField(("Ad Exchange revenue ($)"))
    ad_exchange_average_ecpm = models.FloatField(("Ad Exchange average eCPM ($)"))
    
    def __str__(self):
        return self.country
    