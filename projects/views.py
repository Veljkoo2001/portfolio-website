from django.shortcuts import render

def project_list_view(request):
    # Za sada vraćamo praznu listu, sutra ćemo dodati bazu
    context = {
        'projects': []
    }
    return render(request, 'main/project.html', context)
