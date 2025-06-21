from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import Member




def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_staff.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context,request))
 #'fruits': ['Apple','Banana','Cherry'],
# Create your views here.
