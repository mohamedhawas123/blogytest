from rest_framework import serializers
from account.models import Account


class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={
        'input_type': 'password'
    }, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write': True}
        }

    def save(self):
        accout = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )

        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password': 'must match'})
        accout.set_password(password1)
        accout.save()
        return accout
