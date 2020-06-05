from django.shortcuts import render,redirect
from .models import subcategory
def add_subcat(request):

    if request.method=='POST':
        subcat=request.POST.get('subcatname')
        if(subcategory.objects.filter(cat=catname)):
       
            error="sub-category already exist"
            return render(request,'back/error.html',{'error':error})
        else:
            c=subcategory(cat=catname)
            c.save()
            return redirect(manage_subcat)

    return render(request,"back/addsubcat.html")

def manage_subcat(request):
    subcat=subcategory.objects.all()

    return render(request,"back/managesubcat.html",{'subcat':subcat})