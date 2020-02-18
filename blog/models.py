from django.conf import settings
from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=200)
    explanation = models.CharField(max_length=200, null=True)
    # text = models.TextField()
    text = MarkdownxField('Contents', help_text='To Write with Markdown format')
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.text)