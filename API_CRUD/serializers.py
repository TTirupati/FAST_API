from fastapi_contrib.serializers.common import ModelSerializer

from models import Account


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
