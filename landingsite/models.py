from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class MainSlider(models.Model):
    title = models.CharField(max_length=35)
    content = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/mainslider')
    centered = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class ServicesSlider(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/services")

    def __str__(self):
        return self.title


class CaseStudiesSlider(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/casestudies')
    body = models.CharField(max_length=400)
    blog_body = RichTextUploadingField ()
    publish_date = models.DateField(null=True)
    tag = models.CharField(max_length=20, null=True)
    cover_image = models.ImageField(upload_to='images/casestudies', null=True)
    def __str__(self):
        return self.title



class InitiativeSlider(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/initiatives')
    site_url = models.URLField()

    def __str__(self):
        return self.title




class ClientsSlider(models.Model):
    image = models.ImageField(upload_to='images/clients')




class WordsOfEncouragementSlider(models.Model):
    content = models.CharField(max_length=300)
    person_image = models.ImageField(upload_to="images/wordsofencouragement")
    person_name = models.CharField(max_length=40)
    person_company = models.CharField(max_length=50)

    def __str__(self):
        return self.person_name




class ManagementPeople(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=40)
    photo = models.ImageField(upload_to="images/people")
    message = RichTextField()
    def __str__(self):
        return self.name




class Advisor(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=40)
    photo = models.ImageField(upload_to="images/people")
    message = RichTextField()
    def __str__(self):
        return self.name





class Patron(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=40)
    photo = models.ImageField(upload_to="images/people")
    message = RichTextField()
    def __str__(self):
        return self.name


class OP_ED(models.Model):
    title = models.CharField(max_length=75)
    thumb_image = models.ImageField(upload_to='images/op_ed')
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    link_to_article = models.URLField()

    def __str__(self):
        return self.title



class Magazine(models.Model):
    title = models.CharField(max_length=75)
    thumb_image = models.ImageField(upload_to='images/magazines')
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    link_to_article = models.URLField()

    def __str__(self):
        return self.title




class Interview(models.Model):
    title = models.CharField(max_length=75)
    thumb_image = models.ImageField(upload_to='images/interviews')
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    link_to_article = models.URLField()

    def __str__(self):
        return self.title



class NewsletterSubscriber(models.Model):
    email = models.EmailField()