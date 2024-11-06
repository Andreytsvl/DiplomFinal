from django.db.models import Q


from products_app.models import Products

def q_search(query):
    if query.isdigit() and len(query) <= 6:
        return Products.objects.filter(id=int(query))

    #return Products.objects.filter(description__search=query)# встроенный поиск по целому слову см сеттинг

    keywords = [word for word in query.split() if len(word) > 2]
    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)