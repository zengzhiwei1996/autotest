from Page.Base_Page import BasePage
import unittest
from Seletor.DownGiveSelector import DownGiveSelector


class DownGiveBabyMes(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def fabushiyong(self):
        title = self.get_title()
        print("网页标题为：", title)
        print("点击发布试用")
        self.click(DownGiveSelector.btn_fabushiyong)

    def xianxiamoshi(self):
        print(u'选择线上模式')
        self.click(DownGiveSelector.btn_xianxiamoshi)

    def shiyongleixing(self):
        print(u'点击试用类型')
        self.click(DownGiveSelector.btn_shiyongleixing)

    def chanpinzengsong(self, test):
        print(u'选择产品赠送')
        self.click(DownGiveSelector.select_chanpinzengsong)
        self.get_text1(DownGiveSelector.select_chanpinzengsong, test)

    def chanpinmingcheng(self, chanpinmingcheng):
        print(u'输入产品名称：', chanpinmingcheng)
        self.input_text(DownGiveSelector.input_chanpinname, chanpinmingcheng)

    def baobeizhutu(self, zhutu):
        print(u'上传主图')
        self.input_text(DownGiveSelector.input_chanpinzhutu, zhutu)

    def chanpinjiage(self, jiage):
        print(u'输入产品价格：', jiage)
        self.input_text(DownGiveSelector.input_chanpinjiage, jiage)

    def fabufenshu(self, fabufenshu):
        print(u'输入发布份数：', fabufenshu)
        self.input_text(DownGiveSelector.input_fabufenshu, fabufenshu)

    def btn_lijifabu(self):
        print(u'点击立即发布!')
        self.click(DownGiveSelector.btn_lijifabu)
