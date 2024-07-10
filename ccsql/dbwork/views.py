from django.http import JsonResponse
from dbwork.models import File
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method=="POST":
        try:
            file=request.FILES.get('file')
            file_obj=File(name=file.name,data=file.read())
            file_obj.save()
            return JsonResponse({"message": "Successfully uploaded"})
        except:
            return JsonResponse({"message":"Either the file doesn't exist or the URL is wrong"})

def retrieve(request,filename):
    if request.method=="GET":
        try:
            file_obj=File.objects.filter(name=filename).first()
            file_info={
                "content_type":"application/octet-stream",
                'Content-Disposition':f'attachment; filename={filename}',
                "content": bytes(file_obj.data).decode('utf-8')
            }
            return JsonResponse(file_info)
        except Exception:
            return JsonResponse({"message":"The requested file name was not found"})

@csrf_exempt
def delete(request,filename):
    if request.method=="DELETE":
        try:
            files,_= File.objects.filter(name=filename).delete()
            if files>0:
                return JsonResponse({"message":"Operation complete"})
            else:
                raise Exception
        except Exception:
            return JsonResponse({'message': 'The requested file name was not found'})
