from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now
from books.models import Book


# Create your models here.
class ReviewManager(models.Manager):
    def published(self):
        return self.filter(state='published')


class  Review(models.Model):
    objects = ReviewManager()
    # author = user
    # title
    # content
    # pub_date
    # state - (draft, in_moderation, published)
    # grade
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Author",
        help_text="",
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Book',
        help_text='',
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Title',
        help_text='',
    )
    content = models.TextField(
        blank=False,
        verbose_name='Content',
        help_text='',
    )
    pub_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Publication Timestamp',
        help_text='',
    )
    STATE_CHOICES = (
        ('draft', 'Draft'),
        ('in_moderation', 'In moderation'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    # pozwala ograniczyć i podać konkretne wartości do wyboru w choices poniżej
    )
    state = models.CharField(
        choices=STATE_CHOICES,
        max_length=40,
        null=False,
        blank=False,
        verbose_name='State',
        help_text='',
    )
    grade = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Grade',
        help_text='Values from 1 to 10',
        validators = [
            MinValueValidator(1),
            MaxValueValidator(10),
            ],
    )

    def __str__(self):
        return f'{self.book.title} review by {self.user} ({self.title})'

    def save(self, *args, **kwargs):
        if self.state == 'published' and not self.pub_date:
            self.pub_date = now()

        return super().save(*args, **kwargs)


class Grade(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Author",
        help_text="",
    )
    grade = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Grade',
        help_text='Values from 1 to 10',
        validators = [
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Book',
        help_text='',
    )

    def __str__(self):
        return f'Rating {self.grade}'