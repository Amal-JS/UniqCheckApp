from django.forms import ModelForm
from . models import CustomUser

class Custom_User_Form(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


'''
        #raise validation error such as user exists with this name (normal way Custom user with username already exists --> to change that used this approach)
        def clean(self):
            cleaned_data = super().clean()
            username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            phone = cleaned_data.get('phone')

            if CustomUser.objects.filter(username=username).exists():
                self.add_error('username', 'User with this Username already exists.')
            if CustomUser.objects.filter(email=email).exists():
                self.add_error('email', 'User with this Email already exists.')
            if CustomUser.objects.filter(phone=phone).exists():
                self.add_error('phone', 'User with this Phone already exists.')'''