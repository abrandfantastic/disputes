from django.db import models

class Contacts(models.Model):

    name = models.CharField(max_length=250)
    phone = models.TextField(max_length=100)
    from_email = models.CharField(max_length=250)
    subject = models.TextField()
    message = models.TextField()
    # image = models.ImageField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, auto_now=False)

    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
    class Meta:
    	verbose_name_plural = "Contacts"
	
    def __str__(self):
        return self.from_email

