from basiclogin.models import User

class verification:
    def __init__(self,wifiname,wifipassword) -> None:
        self.wifiname = wifiname
        self.wifipassword = wifipassword
    def verifity(self):
        user = User.objects.filter(wifiname='restuie')
        if( user != None):
            return False