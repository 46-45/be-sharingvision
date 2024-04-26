from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("The title must be at least 20 characters long.")
        return value

    def validate_content(self, value):
        if len(value) < 200:
            raise serializers.ValidationError("The content must be at least 200 characters long.")
        return value

    def validate_category(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("The category must be at least 3 characters long.")
        return value

    def validate_status(self, value):
        valid_statuses = ['publish', 'draft', 'thrash']
        if value not in valid_statuses:
            raise serializers.ValidationError(f"The status must be one of {valid_statuses}.")
        return value
