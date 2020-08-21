from Page.Base_Page import BasePage
from Seletor.Login_Selector import Login
import time


class LoginPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def input_zhanghao(self, zhanghao):
        print(u"输入账号:", zhanghao)
        self.input_text(Login.input_zhanghao, zhanghao)

    def input_mima(self, mima):
        print(u"输入密码:", mima)
        self.input_text(Login.input_mima, mima)

    def btn_denglu(self):
        print(u"点击登录")
        self.click(Login.btn_denglu)

    def btn_queren(self):
        print(u"点击确定")
        self.click(Login.btn_queren)

    def btn_zhidao(self):
        n = 1
        while n < 9:
            print(u"点击", n, "次知道了")
            self.click(Login.btn_zhidao)
            time.sleep(1)
            n = n + 1