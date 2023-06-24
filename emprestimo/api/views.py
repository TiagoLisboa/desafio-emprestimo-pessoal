from .serializers import ProposalSerializer, ProposalFieldSerializer
from .models import ProposalField
from .tasks import evaluate_proposal

from emprestimo.authenticators import CsrfExemptSessionAuthentication

from rest_framework import mixins, generics
from rest_framework.authentication import BasicAuthentication
from django.views.decorators.csrf import csrf_exempt

class CreateProposal(mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = ProposalSerializer
    permission_classes = []
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        evaluate_proposal.delay(response.data['id'])
        return response


class ProposalField(generics.ListAPIView):
    queryset = ProposalField.objects.all()
    serializer_class = ProposalFieldSerializer
