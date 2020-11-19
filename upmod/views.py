from django.http import HttpResponse
from django.shortcuts import render
from .forms import DocumentForm
'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm()
        if form.is_valid():
            # ��ô���Ϳ����ˣ��ļ��ᱻ���浽Model��upload_to����ָ����λ��
            form.save()
            return HttpResponse('Upload Success')
    else:
        form = UploadFileForm()
    return HttpResponse("Upload Failed")
'''

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Upload Success')
    else:
        form = DocumentForm()
    return HttpResponse('Upload Failed')