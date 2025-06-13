from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Job
from .forms import JobForm
from django.contrib import messages

def home(request):
    return render(request, 'jobs/home.html')

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@csrf_exempt
def api_post_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        job = Job.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            skills_required=data.get('skills_required', 'general'),
            is_urgent=data.get('is_urgent', False),
            expiry_date=data.get('expiry_date'),
        )

        return JsonResponse({'message': 'Job posted successfully', 'id': job.id})
    else:
        return JsonResponse({'error': 'Only POST requests allowed'}, status=400)

def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user if request.user.is_authenticated else None
            job.save()
            print("Redirecting to job detail:", job.id)
            return redirect('job_detail', pk=job.id)  # ✅ Fixed to use pk
        else:
            print("Form is invalid:", form.errors)
    else:
        form = JobForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})

def job_detail(request, pk):  # ✅ Unified to use 'pk'
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_detail.html', {'job': job})
