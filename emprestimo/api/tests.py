from django.test import TestCase
from .models import ProposalField

from rest_framework.test import APIClient

class ProposalTestCase(TestCase):
    def setUp(self) -> None:
        ProposalField(name='cpf', field_type=0, is_required=True).save()
        ProposalField(name='Nome Completo', field_type=0, is_required=True).save()
        self.client = APIClient()
        return super().setUp()

    def test_create_proposal(self):
        pass

    def test_create_proposal_validation_failure(self):
        response = client.post('/proposal')
