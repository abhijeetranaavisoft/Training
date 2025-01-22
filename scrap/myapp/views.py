from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import ExtractedContent
from .forms import URLForm

def scrape(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            # Scrape the URL
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            p_tags = soup.find_all('p')
            content = '\n'.join([p.get_text() for p in p_tags])

            # Save to database
            extracted_content = ExtractedContent.objects.create(url=url, content=content)

            # Redirect to the download page after scraping
            return redirect('content', pk=extracted_content.pk)

    else:
        form = URLForm()

    return render(request, 'scrape.html', {'form': form})


def download(request, pk):
    content = ExtractedContent.objects.get(pk=pk)
    contentall=ExtractedContent.objects.all()
    
    # Ensure the content exists
    if content:
        response = HttpResponse(content.content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="extracted_content.txt"'
        return render(request, 'look.html',{'contentall':contentall})
    else:
        return HttpResponse("Content not found", status=404)


def look(request, pk):
    content = ExtractedContent.objects.get(pk=pk)
    
    if content:
        response = HttpResponse(content.content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="extracted_content.txt"'
        return response
    else:
        return HttpResponse("Content not found", status=404)




def content(request, pk):
    content = ExtractedContent.objects.get(pk=pk)
    
    
    # Display a page telling the user that the content is ready to download
    return render(request, 'content.html', {'content': content})
