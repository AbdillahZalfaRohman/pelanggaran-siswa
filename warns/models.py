from django.db import models

# Create your models here.
class Warns(models.Model):
    nama_pelanggaran = models.CharField(max_length=254)
    poin_pelanggaran = models.IntegerField()
    color = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)