
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from .forms import DocumentForm
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
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Upload Success')
        else: 
            print( form.errors.as_text())
            return HttpResponse('POST is good but not success')
    else:
        form = DocumentForm()
    return HttpRequest('Upload Failed')