from django.shortcuts import render,redirect
from .models import main,Trandingpost 
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    post=Trandingpost.objects.all()
    site=main.objects.get(title="Magnews")
    d={'site':site,'post':post}
    return render(request,"home.html",d)
def about(request):
    site=main.objects.get(title="Magnews")
    d={'site':site}
    return render(request,"about.html",d)

def news_details(request,which_news):
    trandingnews=Trandingpost.objects.get(about=which_news)
    #print(trandingnews.title)
    return render(request,"trandingnews_details.html",{"news":trandingnews})

def panel(request):
    return render(request,"back/index.html")

def news_list(request):
    news=Trandingpost.objects.all()

    return render(request,"back/news_list.html",{"news":news})

def news_add(request):
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
       
        writer=request.POST.get('writer')
        newsdetails=request.POST.get('newsdetails')
        pubdate=request.POST.get('pub_date')
        
        #print(newstitle,newscat,writer,newsdetails)
        if newstitle=="" or writer=="" or newsdetails=="" or pubdate=="":
            error="All feilds are required"
            return render(request,"back/error.html",{'error':error})
        try:#to check file is uploaded or not
            image=request.FILES['image']
            f=FileSystemStorage()
            filename=f.save(image.name,image)#set name of image and if already present set some random name
            #url=f.url(filename)#make urls for media folder
            if str(image.content_type).startswith("image"):#to check the type of file uploaded
                if image.size<5000000:#to check the size of image uploaded
                    n=Trandingpost(about=newstitle,img=image,title=newstitle,imgname=filename,pub_date=pubdate,details=newsdetails,writer=writer,views=0)
                    n.save()
                    return redirect(news_list)
                else:
                    
                    f.delete(filename)
                    error="file is too large only support 5MB"
                    return render(request,"back/error.html",{'error':error})

            else:
                f.delete(filename)
                error="file is too large only support 5MB"

                error="File type not supported"
                return render(request,"back/error.html",{'error':error})
    
               
        except:
            
            error="please upload image"
            return render(request,"back/error.html",{'error':error})
    
    
    return render(request,"back/newsadd.html")


def news_delete(request,pk):
    
    news=Trandingpost.objects.get(pk=pk)
    fs=FileSystemStorage()
    fs.delete(news.imgname)
    news.delete()
    
   
    return redirect(news_list)