from django.db import models


class DateTimeAbstractModel(models.Model):

        created_at = models.DateTimeField(verbose_name='Creaion Time', auto_now_add=True)

        class Meta:
                abstract = True


class Contact(DateTimeAbstractModel):
        
        fname = models.CharField(verbose_name='First Name', max_length=255)
        lname = models.CharField(verbose_name='Last Name', max_length=255, blank=True, null=True)
        phone = models.CharField(verbose_name='Mobile Number',max_length=255)
        home = models.CharField(verbose_name='Home Number', max_length=255, blank=True, null=True)
        email = models.EmailField(verbose_name='Email Address', max_length=255,blank=True, null=True)


        def __str__(self):
            return f"{self.fname} {self.lname}"
        