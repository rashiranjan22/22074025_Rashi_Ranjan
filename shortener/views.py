from django.shortcuts import render

from .forms import ShortenURLForm
from .models import ShortURL

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            short_url, created = ShortURL.objects.get_or_create(long_url=long_url)
            short_code=short_url.short_code
            return render(request, 'shortener/shortened_url.html', {'short_url': request.build_absolute_uri(short_url.short_code),'short_code':short_code})
    else:
        form = ShortenURLForm()

    return render(request, 'shortener/shorten_url.html', {'form': form})



from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .models import ShortURL

def redirect_to_original_url(request, short_code):
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        return redirect(short_url.long_url)
    except ShortURL.DoesNotExist:
        return HttpResponseNotFound("Short URL not found")



from .models import ShortURL

def short_url_list(request):
    short_urls = ShortURL.objects.all()
    return render(request, 'shortener/short_url_list.html', {'short_urls': short_urls})
