
from django.http import HttpResponse,HttpRequest
'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm()
        if form.is_valid():
            # 这么做就可以了，文件会被保存到Model中upload_to参数指定的位置
            form.save()
            return HttpResponse('Upload Success')
    else:
        form = UploadFileForm()
    return HttpResponse("Upload Failed")
'''

def model_form_upload(request:HttpRequest):
    def handle_uploaded_file(f):
        with open('/mydata/My_Work/django_project/Upload/upmod/FileStore/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    if request.method=='POST':
        handle_uploaded_file(request.FILES['file'])
        return(HttpResponse("Upload success"))
    else:
        return(HttpResponse("Failed"))