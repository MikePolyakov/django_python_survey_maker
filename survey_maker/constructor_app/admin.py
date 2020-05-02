from django.contrib import admin
from constructor_app.models import Company, Structure, Survey, Question, QuestionType1

# Register your models here.
admin.site.register(Company)
admin.site.register(Structure)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(QuestionType1)
