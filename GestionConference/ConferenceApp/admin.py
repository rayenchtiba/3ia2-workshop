from django.contrib import admin
from .models import conference , submission,OrganizingCommittee
# Register your models here.
admin.site.site_title="Gestion Conference 25/26"
admin.site.site_header="Gestion Conference"
admin.site.index_title="Django App Conference"
admin.site.register(conference)
admin.site.register(submission)
admin.site.register(OrganizingCommittee)
