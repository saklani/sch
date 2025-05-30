from django.http import HttpResponse
from django.db.models import Q
from .models import Book

def test_query_0(request):
    output = []
    output.append("=== All Books ===")
    books = Book.objects.all()
    for b in books:
        output.append(f"{b.title} by {b.author.name} published in {b.published_year}. Genres: {", ".join(b.tags.values_list('name', flat=True))}. Status: {'Out of Print' if b.is_out_of_print else 'In Print'}")
    return HttpResponse("<pre>" + "\n".join(output) + "</pre>")

def test_query_1(request):
    output = []
    
    # ———————————— FK / O2O (single row) ————————————
    output.append("=== Select Related (FK) ===")
    books = Book.objects.select_related('author')[:20]
    for b in books:
        output.append(f"{b.title} by {b.author.name}")
    
    # M2M / reverse FK (collections) 
    output.append("\n=== Prefetch Related (M2M) ===")
    books = Book.objects.prefetch_related('tags')[:20]
    for b in books:
        tags = [t.name for t in b.tags.all()]
        output.append(f"{b.title}: {tags}")
    
    return HttpResponse("<pre>" + "\n".join(output) + "</pre>")

def test_query_2(request):
    output = []
    output.append("=== Q Objects ===")
    # Same in one call (using & operator for AND):
    qs = Book.objects.filter(
        (Q(tags__name='Horror') | Q(tags__name='Fantasy'))
        & ~Q(is_out_of_print=True)
    )
    output.append("Books that are not out of print and are either Horror or Fantasy: " + ", ".join(qs.values_list('title', flat=True)))
    return HttpResponse("<pre>" + "\n".join(output) + "</pre>")

