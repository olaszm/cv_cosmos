from django.contrib import admin

# Register your models here.
from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        # ('Total Votes', {'fields': ['total_votes']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # readonly_fields = ('total_votes',)
    list_display = ('question_text' , 'pub_date')#'total_votes')

admin.site.register(Question,QuestionAdmin)
