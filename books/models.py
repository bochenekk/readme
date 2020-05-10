from django.db import models

# Create your models here.
class Author(models.Model):
    # imię
    # nazwisko
    # data urodzenia
    # strona prywatna

    first_name = models.CharField(
        max_length=50,
        null = False,
        blank = False,
        verbose_name = 'First Name',
        help_text = '',
    )
    last_name = models.CharField(
        max_length=100,
        null = False,
        blank = False,
        verbose_name = 'Last Name',
        help_text = '',
    )
    birth_date = models.DateField(
        null = True,
        blank = True,
        verbose_name = 'Birth Date',
        help_text = '',
    )
    web_site = models.URLField(
        # max_length jest domyślnie ustawiony dla URLField na 200
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Private Website Address',
        help_text = '',
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    # tytuł
    # autor
    # gatunek
    # liczba stron
    # (czas czytania?)
    # opis książki
    # link do zdjęcia książki
    title = models.CharField(
        max_length=100,
        null = False,
        blank = False,
        verbose_name = 'Title',
        help_text = '',
    )
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, # zachowanie bazy danych przy usuwaniu autora,
        # gdy są do niego przypisane jakieś książki - nie da się usunąć
        null = False,
        blank = False,
        verbose_name = 'Author',
        help_text = '',
    )
    categories = models.ManyToManyField(
        'Category',
        blank = False, # wymusi przypisanie książki do co najmniej jednej kategorii
        verbose_name = "Categories",
        help_text = '',
    )
    pages = models.PositiveIntegerField(
        default = 0,
        null = True,
        blank = True,
        verbose_name = 'Number of Pages',
        help_text = '',
    )
    # cover_link = models.ImageField(
    # )
    description = models.TextField(
        blank = True,
        verbose_name = 'Description',
        help_text = '',
    )


class Category(models.Model):
    # nazwa
    # opis kategorii

    name = models.CharField(
        max_length=50,
        null = False,
        blank = False,
        verbose_name = 'Category',
        help_text = '',
    )
    description = models.TextField(
        blank = True,
        verbose_name = 'Description',
        help_text = '',
    )

    def __str__(self):
        return self.name


