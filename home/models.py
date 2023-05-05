from django.db import models
#veritabanındaki ilgili tabloları oluşturmak için kullanılır

class Contact(models.Model):
    name = models.CharField(max_length=100)#formdaki alanlar tanımlanır.
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True) #formu admin panelde görüntülemek için bir model oluşturulur.

    def __str__(self):
        return self.email