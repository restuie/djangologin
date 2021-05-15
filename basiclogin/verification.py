from basiclogin.models import User
#驗證輸入的帳號密碼有沒有重複以及有沒有註冊過
class verification:
    def __init__(self,wifiname,wifipassword) -> None:
        self.wifiname = wifiname
        self.wifipassword = wifipassword
    def verifity(self):
        user = User.objects.filter(wifiname=self.wifiname)
        if( user.count() == 1):
            return user
