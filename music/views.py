from django.shortcuts import render, redirect
from .models import File
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from .models import CustomUser
from .forms import UpdateFileForm


def home(request):
    # public_files = File.objects.filter(
    #     file_status='public').order_by('-upload_date')

    # shared_files = None

    # if request.user.is_authenticated:
    #     shared_files = File.objects.filter(
    #         allowed_emails=request.user.email).order_by('-upload_date')
    #     public_files = public_files.exclude(allowed_emails=request.user.email)

    # context = {
    #     'public_files': public_files,
    #     'shared_files': shared_files
    # }

    files = []

    if request.user.is_authenticated:
        public_files = File.objects.filter(
            file_status='public').order_by('-upload_date')
        shared_files = File.objects.filter(
            allowed_emails=request.user.email).order_by('-upload_date')

        for file in public_files:
            files.append({
                'file': file,
                'is_shared': False
            })

        for file in shared_files:
            files.append({
                'file': file,
                'is_shared': True
            })

        files.sort(key=lambda x: x['file'].upload_date, reverse=True)
        print(files)

    else:
        public_files = File.objects.filter(
            file_status='public').order_by('-upload_date')
        for file in public_files:
            files.append({
                'file': file,
                'is_shared': False
            })

    context = {
        'files': files
    }

    return render(request, 'home.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            audio_file = form.cleaned_data['audio_file']
            file_status = form.cleaned_data['file_status']
            owner = request.user
            allowed_emails = []
            if file_status == 'protected':
                allowed_emails = form.cleaned_data['allowed_emails']
                for email in allowed_emails:
                    if not CustomUser.objects.filter(email=email).exists():
                        allowed_emails.remove(email)

            # Save
            file = File.objects.create(
                file_name=file_name,
                audio_file=audio_file,
                file_status=file_status,
                owner=owner
            )
            file.allowed_emails.set(allowed_emails)

            return redirect('home')
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})


@login_required
def delete_file(request, file_id):
    file = File.objects.get(pk=file_id)
    if request.user == file.owner:
        file.delete()
    return redirect('home')


@login_required
def my_files(request):
    uploaded_files = File.objects.filter(owner=request.user)
    return render(request, 'my_files.html', {'uploaded_files': uploaded_files})
