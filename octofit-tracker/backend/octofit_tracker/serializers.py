from rest_framework import serializers

# User Serializer
class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    team = serializers.CharField(max_length=50)

# Team Serializer
class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=100))

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    activity = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

# Leaderboard Serializer
class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField(max_length=100)
    score = serializers.IntegerField()

# Workout Serializer
class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    level = serializers.CharField(max_length=50)
