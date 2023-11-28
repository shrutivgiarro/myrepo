from rest_framework import serializers

from UsersApp.models import User, Logs, Pages


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('user_id', 'email', 'firstname', 'lastname', 'password')

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs 
        fields=('log_id', 'user_id', 'log_in_time', 'log_out_time')

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages 
        fields=('page_visit_id', 'user_id', 'log_id', 'page_name', 'start_time', 'end_time','time_spent')