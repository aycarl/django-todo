from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model.
    """

    class Meta:
        model = Todo
        fields = '__all__'
