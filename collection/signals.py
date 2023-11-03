from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector

from .models import Elemento

@receiver(post_save, sender=Elemento)
def update_search_vector(sender, instance, **kwargs):
    instance.search_vector = SearchVector('nombre', 'categorias', 'etiquetas')
    instance.save()
