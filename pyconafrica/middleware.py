"""
Middleware to redirect all requests to africa.pycon.org
"""
from django.http import HttpResponsePermanentRedirect


class RedirectToAfricaMiddleware:
    """
    Middleware that redirects all requests to africa.pycon.org
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Redirect all requests to africa.pycon.org
        redirect_url = f"https://africa.pycon.org{request.path}"
        if request.GET:
            # Preserve query parameters if any
            query_string = request.GET.urlencode()
            redirect_url = f"{redirect_url}?{query_string}"
        
        return HttpResponsePermanentRedirect(redirect_url)


class RedirectFromAfricaMiddleware:
    """
    Middleware that redirects specific paths from africa.pycon.org to pyconafrica.pythonanywhere.com
    Handles redirects for:
    - /2024/ => https://pyconafrica.pythonanywhere.com/2024/
    - /2020/ => https://pyconafrica.pythonanywhere.com/2020/
    - /2019/ => https://pyconafrica.pythonanywhere.com/2019/
    """
    REDIRECT_PATHS = ['/2024/', '/2020/', '/2019/']
    TARGET_DOMAIN = 'https://pyconafrica.pythonanywhere.com'
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if request is coming from africa.pycon.org
        host = request.get_host()
        
        # Check if host is africa.pycon.org (with or without www)
        if host in ['africa.pycon.org', 'www.africa.pycon.org']:
            # Check if path matches any of the redirect paths
            path = request.path
            if path in self.REDIRECT_PATHS or path.startswith('/2024/') or path.startswith('/2020/') or path.startswith('/2019/'):
                redirect_url = f"{self.TARGET_DOMAIN}{path}"
                if request.GET:
                    # Preserve query parameters if any
                    query_string = request.GET.urlencode()
                    redirect_url = f"{redirect_url}?{query_string}"
                
                return HttpResponsePermanentRedirect(redirect_url)
        
        # If no redirect needed, continue with normal request processing
        return self.get_response(request)
