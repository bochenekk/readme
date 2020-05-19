from django.db import models

# Create your models here.
class Author(models.Model):
    # imię
    # nazwisko
    # data urodzenia
    # strona prywatna

    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='First Name',
        help_text='',
    )
    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Last Name',
        help_text='',
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Birth Date',
        help_text='',
    )
    web_site = models.URLField(
        # max_length jest domyślnie ustawiony dla URLField na 200
        # bazuje na CharField
        null=False,
        blank=True,
        default='',
        verbose_name='Private Website Address',
        help_text='',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
        null=False,
        blank=False,
        verbose_name='Title',
        help_text='',
    )
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, # zachowanie bazy danych przy usuwaniu autora,
        # gdy są do niego przypisane jakieś książki - nie da się usunąć
        # dodaje automatycznie Author.book_set - relation manager
        # a1.book_set.filter(pages__lt=100) , a1 - instancja Author
        null=False,
        blank=False,
        verbose_name='Author',
        help_text='',
    )
    categories = models.ManyToManyField(
        'Category', # w ciapkach bo zdefiniowane dopiero poniżej, ale dzięki
        # temu interpreter jest w stanie mimo wszystko stworzyć relację
        blank=False, # wymusi przypisanie książki do co najmniej jednej kategorii
        verbose_name="Categories",
        help_text='',
    )
    pages = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Number of Pages',
        help_text='',
    )
    # cover_link=models.ImageField(
    # )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    cover = models.ImageField(
        # typ CharField
        blank=True,
        null=False,
        default='',
        verbose_name='Cover image',
        help_text='',
    )

    def get_categories(self):
        return "\n".join([str(p) for p in self.categories.all()])

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    # nazwa
    # opis kategorii

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        help_text='',
        verbose_name='Category',

    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'





