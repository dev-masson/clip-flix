from .models import Clip, Episode

def list_recent_clips(request):
    list_recent = Clip.objects.all().order_by('-created_at')[:10]
    if list_recent:
        list_recent = list_recent
    else:
        list_recent = None
        
    return {"list_recent_clips": list_recent}

def list_clip_popular(request):
    list_popular = Clip.objects.all().order_by('-views')[:10]
    return {"list_clip_popular": list_popular}

def clip_primary(request):
    clip_primary = Clip.objects.filter(id=3).first()
    return {"clip_primary": clip_primary}