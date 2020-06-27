from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': { 'write_only': True},
            # 'email': {'unique': True},
        }


    def save(self):
        account = Account(
            username = self.validated_data['username'],
            email = self.validated_data['email'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
            'password': 'password doesn\'t match!'
        })

        account.set_password(password)
        account.is_active = False
        account.save()
        return account