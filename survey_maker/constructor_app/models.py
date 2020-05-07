from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from users_app.models import SurveyUser


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(null=True, blank=True, upload_to='company')
    user = models.ManyToManyField(SurveyUser, blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'компании'

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    question_type_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'типы вопросов'

    def __str__(self):
        return self.question_type_name


class Question(models.Model):
    question_name = models.CharField(max_length=128)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.question_name


class Page(models.Model):
    greeting = models.CharField(max_length=64, null=True, blank=True)
    instruction = models.CharField(max_length=64, null=True, blank=True)
    final_page = models.CharField(max_length=64, null=True, blank=True)
    page_number = models.PositiveIntegerField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.question_name


class Survey(models.Model):
    name = models.CharField(max_length=64)
    company = models.ManyToManyField(Company)
    start_date = models.DateField()
    end_date = models.DateField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.name


class Structure(MPTTModel):
    company = models.ManyToManyField(Company)
    department = models.CharField(max_length=64, unique=True)
    head_of_department = models.CharField(max_length=64, null=True, blank=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    workers = models.PositiveIntegerField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Структура'
        verbose_name_plural = 'Структуры'

    class MPTTMeta:
        order_insertion_by = ['department']

    def __str__(self):
        return self.department
