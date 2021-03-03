from django.contrib import admin
from .models import Question,Answer,Complain
# Register your models here.
admin.site.register(Question)
admin.site.register(Complain)
admin.site.register(Answer)