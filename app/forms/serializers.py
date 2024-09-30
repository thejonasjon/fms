from rest_framework import serializers
from .models import Form, Field, Response

class FieldSerializer(serializers.Serializer):
    """Serializer for Field."""

    name = serializers.CharField(max_length=200)
    type = serializers.ChoiceField(choices=Field.FIELD_TYPES)
    required = serializers.BooleanField(default=True)


class FormSerializer(serializers.Serializer):
    """Serializer for Form."""

    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False)
    fields = FieldSerializer(many=True)

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')

        form = Form(**validated_data)
        form.fields = [Field(**field) for field in fields_data]

        form.save()
        return form

    def update(self, instance, validated_data):
        fields_data = validated_data.pop('fields', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        instance.fields = [Field(**field) for field in fields_data]
        instance.save()
        return instance


class FormNestedSerializer(serializers.Serializer):
    """Serializer for NestedForm."""

    id = serializers.CharField()
    title = serializers.CharField()

class ResponseSerializer(serializers.Serializer):
    """Serializer for Response."""

    id = serializers.CharField(read_only=True)
    form = FormNestedSerializer()
    responses = serializers.DictField()

    def create(self, validated_data):
        form_id = validated_data.get('form')['id']
        try:
            form = Form.objects.get(pk=form_id)
        except Form.DoesNotExist:
            raise serializers.ValidationError("Form with this ID does not exist.")

        response = Response(
            form=form,
            responses=validated_data.get('responses')
        )
        response.save()
        return response