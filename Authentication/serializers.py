from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomToken_Serializer(TokenObtainPairSerializer):

    def validate(self,attrs):
        data= super().validate(attrs)

        data.update({
            'username':self.user.username,
            'date_joined':self.user.date_joined
        })

        return data