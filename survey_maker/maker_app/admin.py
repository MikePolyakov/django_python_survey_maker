from django.contrib import admin
from maker_app.models import Company, Survey, Question, QuestionType, Structure
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Company)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(QuestionType)

admin.site.register(Structure, MPTTModelAdmin)
