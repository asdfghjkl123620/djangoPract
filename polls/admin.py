from django.contrib import admin

# Register your models here.
from .models import Choice, Question

#告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 4 个足够的选项字段。”
#透過TabularInline代替StackedInline以一種表格式的展示方式顯得更加緊湊
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)