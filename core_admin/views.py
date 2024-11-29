from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required 
def custom_admin_view(request):
    context = {
        "title": "Page personnalisée dans l'admin",
        "extra_data": "Voici une page entièrement personnalisée intégrée dans l'administration Django avec Grappelli.",
    }
    return TemplateResponse(request, "admin/custom_page.html", context)
