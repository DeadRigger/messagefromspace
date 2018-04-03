from django.http import HttpResponse
from django.core import serializers
from .models import Message

def api(request):
    if(request.GET.get('get_messages', '')):
        msg = Message.objects.filter(id__gt=request.GET.get('get_messages', ''))
        data = serializers.serialize('json', msg)
        return HttpResponse(data, content_type='application/json')
    else:
        if(request.GET.get('mark_read', '')):
            Message.objects.filter(id=request.GET.get('mark_read', '')).update(check=True)
        else:
            msg = Message.objects.all().order_by('-id')
            data = serializers.serialize('json', msg)
            return HttpResponse(data, content_type='application/json')