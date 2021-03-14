from django.db import models
from django.core.serializers import serialize
import json


class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def total_votes(self):
        choices = Choice.objects.all().filter(question=self.pk).values('votes')
        total = 0
        for item in choices:
            total += item['votes']
        return total
    
    def get_choices(self):
        choices = Choice.objects.all().filter(question=self.pk)
        return choices


    def serialize(self):
        json_data = serialize('json', [self])
        deserialized = json.loads(json_data)
        obj = deserialized[0]
        obj['fields']['total_votes'] = self.total_votes()
        choies = self.get_choices()
        obj['fields']['choices'] = choies.serialize()
        final_json = json.dumps([{'data': obj['fields']}])
        return final_json

    def __str__(self):
        return self.question_text


class ChoiceQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('choice_text','votes'))
        return list_values
   

class ChoiceManager(models.Manager):
    def get_queryset(self):
        return ChoiceQuerySet(self.model, using=self._db)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    objects = ChoiceManager()

    def __str__(self):
        return self.choice_text


    def serialize(self):
        json_data = serialize('json', [self], fields=('choice_text','votes'))
        return json_data

