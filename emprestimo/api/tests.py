from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch

from .models import ProposalField, Proposal


class ProposalTestCase(TestCase):
    def setUp(self) -> None:
        ProposalField(name='cpf', field_type=0, is_required=True).save()
        ProposalField(name='Nome Completo', field_type=0, is_required=True).save()
        self.client = APIClient()
        return super().setUp()

    @patch('api.views.evaluate_proposal')
    def test_create_proposal(self, mock_task):
        data = {
            'cpf': 12345678901,
            'Nome Completo': 'Fulano de Tal',
        }
        response = self.client.post('/api/proposal', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        proposta_criada = Proposal.objects.get(fields__cpf='12345678901')
        self.assertEqual(proposta_criada.status, 'Não Avaliada')
        self.assertTrue(mock_task.delay.called)

    def test_create_proposal_validation_failure(self):
        data = {}
        response = self.client.post('/api/proposal', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
