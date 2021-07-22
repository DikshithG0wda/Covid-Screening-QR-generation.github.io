from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.http import HttpResponse

def home(request):
    context={}
    L=[]
    s="%"
    if request.method=="POST":
            nam=request.POST['Nam']
            ent=request.POST['entry']
            usn=request.POST.get('uf', False)
            num=request.POST['phone']
            em=request.POST['email']
            if usn==False:
                usn='NA'
            else:
                pass     
            for i in (ent,nam,usn,num,em):
               L.append(i)
            A=L[0]
            L=s.join(L)
            factor=qrcode.image.svg.SvgImage
            img=qrcode.make(L, image_factory=factor,box_size=20)
            stream=BytesIO()
            img.save(stream)
            context["svg"]=stream.getvalue().decode
    else:
        pass
        
    return render(request,"home1.html",context=context)

#def qr(request):
        #context={}
       # L=[]
        #s="%"
        #if request.method=="POST":
            #nam=request.POST['Nam']
           # ent=request.POST['entry']
            #usn=request.POST['uf']
           # num=request.POST['phone']
            #em=request.POST['email']
            #for i in (nam,ent,usn,num,em):
                #L.append(i)

           # L=s.join(L)
           # factor=qrcode.image.svg.SvgImage
            #img=qrcode.make(L, image_factory=factor,box_size=20)
            #stream=BytesIO()
           # img.save(stream)
           # context["svg"]=stream.getvalue().decode
        #else:
            # pass
        

        #return render(request,"qr_code.html",context=context)   