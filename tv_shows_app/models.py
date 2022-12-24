from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['release_date'])== 0 or len(postData['title'])== 0 or len(postData['network'])== 0:
            errors["missing_field"] = "* fields are required"
            return errors
        if 0 < len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if 0 < len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if 0 < len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if postData['release_date']:
            
            new_date=postData['release_date']
            if new_date > datetime.now().strftime("%Y-%m-%d"):
                errors["release_date"] = "Release date should be in the past"
        return errors


class Show(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.DateField(null=True)
    network=models.CharField(max_length=255,null=True)
    desc=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()

class Network(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def get_all_shows():
    return Show.objects.all()

def create_show(showdata):

    title=showdata['title']
    desc=showdata['description']
    network=showdata['network']
    release_date=showdata['release_date']
    return Show.objects.create(title=title,desc=desc,network=network,release_date=release_date)

def update_show(showdata,showid):
    updated_show=Show.objects.get(id=showid)
    updated_show.title=showdata['title']
    updated_show.desc=showdata['description']
    updated_show.network=showdata['network']
    updated_show.release_date=showdata['release_date']
    updated_show.save()

    return updated_show

def delete_show(showid):
    print("test2")
    this_show=Show.objects.get(id=showid)
    this_show.delete()

def get_show(showid):

    show=Show.objects.get(id=showid)
    show.release_date=change_date_format(show.release_date)
    show.updated_at=change_date_format(show.updated_at)
    return show

def change_date_format(date):
    new_date=date.strftime("%Y-%m-%d")
    return new_date
    