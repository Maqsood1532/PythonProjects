from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    now = datetime.now()

    return render(
            request,
            'ReportingApp/index.html',
            {
                'title': "Reporting App",
                'message': " Hello Maqsood",
                'content': " on " + now.strftime("%A, %d %B, %Y at %X")
            }
        )
