from .serializers import ProposalSerializer

from rest_framework import mixins, generics

class CreateProposal(mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = ProposalSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
