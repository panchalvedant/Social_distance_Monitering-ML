from django.shortcuts import render
from django.core.files.base import ContentFile
from .models import Video
from .forms import VideoForm
import os
from django.db import models 

def Home(request):
    lastvideo= Video.objects.last()
    if lastvideo!=None:
        videofile= lastvideo.videofile
    else:
        videofile=None
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        name=form.cleaned_data.get('name')
        os.system(f"python .\\core\\SocialDistancing\\run.py -i .\\media\\videos\\{name}.mp4")
        #os.system(f"python .\\core\\bd\\social_distance_detector.py --input  .\\media\\videos\\{name}.mp4 --output .\\media\\videos\\output.avi  --display 1") 
    context= {'videofile': videofile,
              'form': form
              }
    #subprocess.run(["python C:\\Users\\Admin\\Desktop\\sd\\core\\social_distance_detector.py", "--input C:\\Users\\Admin\\Desktop\\sd\\media\\videos\\New1.mp4","--output C:\\Users\\Admin\\Desktop\\sd\\media\\videos\\output.avi"])
    
    return render(request,'index.html',context)