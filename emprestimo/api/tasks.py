from .models import Proposal
from celery import shared_task

import random

@shared_task
def evaluate_proposal(proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)
    status = ['Aprovada', 'Reprovada']
    proposal.status = random.choice(status)
    proposal.save()
