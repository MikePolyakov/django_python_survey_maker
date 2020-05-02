from django.db import models


# Create your models here.
class QuestionType1(models.Model):
    type_1 = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_type_1 = models.ForeignKey(QuestionType1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    questions = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Structure(models.Model):
    department = models.CharField(max_length=64)
    code = models.PositiveIntegerField(null=True)
    workers = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)
    structure = models.ForeignKey(Structure, on_delete=models.DO_NOTHING)
    surveys = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
