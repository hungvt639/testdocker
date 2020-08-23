from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import Hello, Nguoi
# Create your views here.


class hello(View):
    def get(self, request):
        hellos = Hello.objects.all()
        return render(request, 'hello.html', {"hellos": hellos})

    def post(self, request):
        try:
            h = Hello()
            h.head = request.POST['head']
            h.context = request.POST['context']
            h.save()
            return redirect('hello')
        except:
            return redirect('sos')


class sos(View):
    def get(self, request):
        return HttpResponse("404")


class create_superuser(View):
    def get(self, request):
        superuser = User.objects.filter(username="vth").first()
        if superuser:
            return redirect('sos')
        else:
            User.objects.create_superuser(username='vth', password='Hung12345')
            return redirect('hello')


class xam_xi(View):
    def get(self, request):
        return render(request, 'xam_xi.html')

    def post(self, request):
        try:
            nguoi = Nguoi()
            nguoi.name = request.POST['name']
            nguoi.age = request.POST['age']
            nguoi.save()
            nguois = Nguoi.objects.all()
            return render(request, 'xam_xi_du.html', {"nguoi": nguoi, "nguois": nguois})
        except Exception as e:
            raise e