from django.shortcuts import render,redirect
from .models import category
def add_cat(request):

    if request.method=='POST':
        catname=request.POST.get('catname')
        if(category.objects.filter(cat=catname)):
       
            error="category already exist"
            return render(request,'back/error.html',{'error':error})
        else:
            c=category(cat=catname)
            c.save()
            return redirect(manage_cat)

    return render(request,"back/addcat.html")

def manage_cat(request):
    cat=category.objects.all()

    return render(request,"back/managecat.html",{'cat':cat})