from django.shortcuts import render


def index(request):
    """Home page view - redirects to coming soon page"""
    return render(request, 'bns_coming_soon.html')
def main(request):
    """Home page view - redirects to coming soon page"""
    return render(request, 'main.html')

def coming_soon(request):
    """Coming soon page view"""
    return render(request, 'bns_coming_soon.html')


def budget_ndio_story(request):
    """Budget NDIO story page view"""
    return render(request, 'budget_ndio_story.html')


def option1(request):
    """Option 1 page view"""
    return render(request, 'option1.html')


def option2(request):
    """Option 2 page view"""
    return render(request, 'option2.html')


def option3(request):
    """Option 3 page view"""
    return render(request, 'option3.html')


def option4(request):
    """Option 4 page view"""
    return render(request, 'option4.html')


def bnsclaude(request):
    """BNS Claude page view"""
    return render(request, 'bnsclaude.html')

