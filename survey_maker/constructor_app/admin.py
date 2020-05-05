from django.contrib import admin
from constructor_app.models import Company, Survey, Question, QuestionType, UserCategory, User
from mptt.admin import MPTTModelAdmin
from constructor_app.models import Structure


# Register your models here.
admin.site.register(Company)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(UserCategory)
admin.site.register(User)

admin.site.register(Structure, MPTTModelAdmin)
