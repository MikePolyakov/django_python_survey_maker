from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class QuestionType(models.Model):
    question_type_name = models.CharField(max_length=64)

    def __str__(self):
        return self.question_type_name


class Question(models.Model):
    question_name = models.CharField(max_length=128)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name


class Survey(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Structure(MPTTModel):
    department = models.CharField(max_length=64, unique=True)
    head_of_department = models.CharField(max_length=64, null=True, blank=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    workers = models.PositiveIntegerField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['department']

    def __str__(self):
        return self.department


class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    surveys = models.ManyToManyField(Survey)
    logo = models.ImageField(null=True, blank=True, upload_to='company')

    def __str__(self):
        return self.name
