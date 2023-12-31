from .models import Proposal, ProposalField
from rest_framework import serializers

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'status']

    def __init__(self, *args, **kwargs):
        super(ProposalSerializer, self).__init__(*args, **kwargs)

        fields = ProposalField.objects.all()
        for field in fields:
            if (field.field_type == ProposalField.TYPE_STRING):
                new_field = serializers.CharField(required=field.is_required)
            elif (field.field_type == ProposalField.TYPE_INTEGER):
                new_field = serializers.IntegerField(required=field.is_required)
            elif (field.field_type == ProposalField.TYPE_FLOAT):
                new_field = serializers.FloatField(required=field.is_required)
            elif (field.field_type == ProposalField.TYPE_BOOLEAN):
                new_field = serializers.BooleanField(required=field.is_required)
            else:
                new_field = serializers.CharField(required=field.is_required)

            self.fields[field.name] = new_field

    def create(self, validated_data):
        return Proposal.objects.create(fields=validated_data)


class ProposalFieldSerializer(serializers.ModelSerializer):
    field_type = serializers.SerializerMethodField()

    class Meta:
        model = ProposalField
        fields = '__all__'

    def get_field_type(self, obj):
        return obj.get_field_type_display()

