from django.contrib.auth.models import User

class EmailAuthBackend:
    """
    使用电子邮件地址作为用户名验证登录
    """
    def authenticate(self,request,username=None,password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None


