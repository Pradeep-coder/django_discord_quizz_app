from attr import fields
from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question',
    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer',
        'is_correct'
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'points',
        'difficulty',
    ]
    list_display = [
        'title',
        'updated_at'
    ]
    inlines = [
        AnswerInlineModel,
    ]

