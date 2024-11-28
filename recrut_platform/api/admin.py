from django.contrib import admin
from .models import Candidate, Recruiter, JobOffer, Application, Company

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(JobOffer)
admin.site.register(Application)
admin.site.register(Company)