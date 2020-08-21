from Page.Base_Page import BasePage
import unittest
from Seletor.UpUseSelector import BaobeiPage
from Seletor.UpUseSelector import SousuoPage1
from Seletor.UpUseSelector import SousuoPage2
from Seletor.UpUseSelector import FabuPage


class Baobeixinxi(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def fabushiyong(self):
        title = self.get_title()
        print("网页标题为：", title)
        print("点击发布试用")
        self.click(BaobeiPage.btn_fabushiyong)

    def xianshangmoshi(self):
        print(u'选择线上模式')
        self.click(BaobeiPage.btn_xianshangmoshi)

    def shiyongleixing(self):
        print(u'点击试用类型')
        self.click(BaobeiPage.btn_shiyongleixing)

    def chanpingzengsong(self, test):
        print(u'选择产品赠送')
        self.click(BaobeiPage.select_chanpingzengsong)
        self.get_text1(BaobeiPage.select_chanpingzengsong, test)

    def suoshudianpu(self):
        print(u"点击所属店铺")
        self.click(BaobeiPage.btn_suoshudianpu)

    def diyijianpu(self, test):
        print(u"选择第一间铺")
        self.click(BaobeiPage.select_dianpu)
        self.get_text1(BaobeiPage.select_dianpu, test)

    def baobeilianjie(self, lianjie):
        print(u"输入宝贝链接：", lianjie)
        self.input_text(BaobeiPage.input_baobeilianjie, lianjie)

    def baobeibiaoti(self, biaoti):
        print(u"输入宝贝标题：", biaoti)
        self.input_text(BaobeiPage.input_baobeibiaoti, biaoti)

    def baobeizhutu(self, zhutu):
        print(u'上传主图')
        self.input_text(BaobeiPage.input_baobeizhutu, zhutu)

    def skutu(self, sku):
        print(u'上传sku图')
        self.input_text(BaobeiPage.input_skutu, sku)

    def zhanshijia(self, zhanshijia):
        print(u'输入展示价：', zhanshijia)
        self.input_text(BaobeiPage.input_zhanshijia, zhanshijia)

    def chengjiaojia(self, chengjiaojia):
        print(u'输入成交价：', chengjiaojia)
        self.input_text(BaobeiPage.input_chengjiaojia, chengjiaojia)

    def zhuyishixiang(self, zhuyishixiang):
        print(u'输入注意事项：', zhuyishixiang)
        self.input_text(BaobeiPage.input_zhuyishixiang, zhuyishixiang)

    def btn_baobeixinxi(self):
        print(u'点击确认!')
        self.click(BaobeiPage.btn_baobeixinxi)

    def tishi(self, test):
        print(u'判断提示语是否正确:')
        self.get_text1(BaobeiPage.tip_tishi, test)

    # ------------------------------------分割线------------------------------------------------------


class xxsy_Sousuo1(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def shoujiban(self):
        print(u"点击手机版")
        self.click(SousuoPage1.btn_shoujiban)

    def diannaoban(self):
        print(u"点击电脑版")
        self.click(SousuoPage1.btn_diannaoban)

    def guanjianci(self):
        print(u"选择关键词")
        self.click(SousuoPage1.btn_guanjianci)

    def guanjianci1(self, guanjianci):
        print(u"输入关键词1：", guanjianci)
        self.input_text(SousuoPage1.input_guanjianci1, guanjianci)

    def guanjianci2(self, guanjianci):
        print(u"输入关键词2：", guanjianci)
        self.input_text(SousuoPage1.input_guanjianci2, guanjianci)

    def guanjianci3(self, guanjianci):
        print(u"输入关键词3：", guanjianci)
        self.input_text(SousuoPage1.input_guanjianci3, guanjianci)

    def sousuopaixu(self):
        print(u"选择搜索排序")
        self.click(SousuoPage1.btn_sousuopaixu)

    def xiaoliang(self):
        print(u"选择 销量")
        self.click(SousuoPage1.select_xiaoliang)

    def zonghe(self):
        print(u"选择 综合")
        self.click(SousuoPage1.select_zonghe)

    def zhitongche(self):
        print(u"选择 直通车")
        self.click(SousuoPage1.select_zhitongche)

    def fukuanshijian(self):
        print(u"付款时间")
        self.click(SousuoPage1.btn_fukuanshijian)

    def shijian1(self):
        print(u"选择6小时")
        self.click(SousuoPage1.select_shijian1)

    def dangqianxiaoliang(self, xiaoliang):
        print(u'输入当前销量：', xiaoliang)
        self.input_text(SousuoPage1.input_xiaoliang, xiaoliang)


class Sousuo2(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


class Fabu(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def fabufenshu(self, fabufenshu):
        print(u"输入发布份数：", fabufenshu)
        self.input_text(FabuPage.input_fabufenshu, fabufenshu)

    def paixiajianshu(self, paixiajianshu):
        print(u"输入拍下件数：", paixiajianshu)
        self.input_text(FabuPage.input_paixiajianshu, paixiajianshu)

    def lijifabu(self):
        self.click(FabuPage.btn_lijifabu)
