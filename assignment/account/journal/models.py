from django.db import models

# Create your models here.
class journal(models.Model):
    explanation=models.CharField(max_length=200,blank=False)
    debit=models.IntegerField()
    credit=models.IntegerField()
    balance=models.DecimalField(max_digits=8,decimal_places=2)


    class Meta:
        db_table="journal"