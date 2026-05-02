from django.shortcuts import render
from gallery.models import GalleryLook

def home(request):
    gallery_looks = GalleryLook.objects.prefetch_related('media_items').order_by('-created_at')
    return render(request, 'core/home.html', {
        'gallery_looks': gallery_looks,
        'test_message': 'VIEW IS CONNECTED'
    })

def contact(request):
    return render(request, 'core/contact.html')    