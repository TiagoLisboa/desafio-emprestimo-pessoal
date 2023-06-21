from django.contrib import admin

from .models import ProposalField, Proposal

# Register your models here.
admin.site.register(ProposalField)
admin.site.register(Proposal)
