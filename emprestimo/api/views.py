from .serializers import ProposalSerializer
from .tasks import evaluate_proposal

from rest_framework import mixins, generics

class CreateProposal(mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = ProposalSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        evaluate_proposal.delay(response.data['id'])
        return response
