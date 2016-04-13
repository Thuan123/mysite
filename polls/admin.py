from django.contrib import admin

# Register your models here.
from .models import Question,Category,Answer,Exam,Result
#from .models import Choice

"""class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3"""

class QuestionAdmin(admin.ModelAdmin):
    """list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]"""
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Exam)
admin.site.register(Result)
