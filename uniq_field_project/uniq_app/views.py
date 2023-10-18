from django.http import JsonResponse
from django.shortcuts import redirect, render
from . models import CustomUser
from . forms import Custom_User_Form
# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form = Custom_User_Form(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('success')
        else:
            
            
            return render(request,'signup.html',{'form':form})
    form = Custom_User_Form()
    return render(request,'signup.html',{'form':form})


def success(request):
    return render(request,'success.html')
    
def uniq_check(request):
    
    field_name = request.GET.get('field_name',None)
    field_value = request.GET.get('field_value',None)
    error_list=''
    print('comes')

    if field_name == 'username':


        if field_value == '':
            error_list += ',Username required'

        elif len(field_value)<5 and len(field_value)>0:
                error_list += ",Username atleast 5 characters"

       
        if len(field_value)>0:
             if not field_value[0].isupper():
                error_list += ",Username first letter must be capital"

        if len(field_value)>0 and  CustomUser.objects.filter(username=field_value).exists():
                    error_list = "Username already exists"

    elif field_name == 'email':

        if field_value == '':
            error_list += 'Email required'

        elif '@' not in field_value or '.' not in field_value:
            error_list += ",Enter valid Email"
        
        if len(field_value) >0 and CustomUser.objects.filter(email=field_value).exists():
            error_list += ",Email already exists"
        
           

    elif field_name == 'phone':

        if field_value == '':
            error_list += ',Phone Number required'
         
        elif len(str(field_value))>0 and len(str(field_value))<10:
            error_list += ",Phone Number must have 10 numbers"

        

        elif CustomUser.objects.filter(phone=field_value).exists():
           error_list += ",Phone Number already exists"
        
    
    if error_list == '':  
        return JsonResponse({'exists':False})
    
        
    else:
        errors = { field_name:error_list }
        return JsonResponse({'exists':True,'errors':errors})