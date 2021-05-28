from django.views.generic import TemplateView

class LoginView(TemplateView):
    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')

        print(email)
        print(password)

class RegisterView(TemplateView):
    template_name = 'pages/auth.html'
