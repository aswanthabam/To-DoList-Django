class ToastMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        toast = request.session.get("toast")
        if toast:
            count = request.session.get("toast-count")
            print(count)
            if not count:
                request.session["toast-count"] = "0"
            else:
                request.session['toast'] = None
                request.session['toast-count'] = None
        response = self.get_response(request)
        
        return response