from django.db import models
from django.contrib.auth.models import User

class dataa(models.Model):
    s_no=models.IntegerField(primary_key=True)
    entity=models.CharField(max_length=50,blank=True,default=False)
    total_count=models.IntegerField(default=True)
    entity_sections=models.CharField(max_length=100,blank=True,default=False)
    organisation_name=models.CharField(max_length=100,blank=True,default=True)
    doctor_name=models.CharField(max_length=100,blank=True,default=True)
    recommended_coding_system=models.CharField(max_length=30,blank=True,default=True)
    recommended_code=models.CharField(max_length=30,blank=True,default=True)
    recommended_token=models.CharField(max_length=100,default=True)
    is_recommended=models.BooleanField(default=True)
    correct_text = models.CharField(max_length=100, blank=True, default=True)
    code=models.CharField(max_length=100)
    applicable_for_which=models.CharField(max_length=100,blank=True,default=True)
    is_submit=models.BooleanField(default=True)
    is_verify=models.BooleanField(default=True)
    flag_for_discussion=models.BooleanField(default=True)
    submit_username=models.CharField(max_length=100)
    verify_username=models.CharField(max_length=100)
    class Meta:
        db_table="after_lockdown"


class User_check(models.Model):

    user_name=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

    class Meta:
        db_table='user_checking'