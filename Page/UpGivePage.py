from Page.Base_Page import BasePage
import unittest
from Seletor.UpGiveSelector import UpGiveSelector


class UpGiveBabyMes(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def fabushiyong(self):
        title = self.get_title()
        print("网页标题为：", title)
        print("点击发布试用！")
        self.click(UpGiveSelector.btn_fabushiyong)

    def xianshangmoshi(self):
        print(u'选择线上模式！')
        self.click(UpGiveSelector.btn_xianshangmoshi)

    def shiyongleixing(self):
        print(u'点击试用类型！')
        self.click(UpGiveSelector.btn_shiyongleixing)

    def chanpinzengsong(self, test):
        print(u'选择产品赠送！')
        self.click(UpGiveSelector.select_chanpingzengsong)
        self.get_text1(UpGiveSelector.select_chanpinzengsong, test)

    def suoshudianpu(self):
        print(u"点击所属店铺！")
        self.click(UpGiveSelector.btn_suoshudianpu)

    def dianpu(self, test):
        print(u"选择第一间铺！")
        self.click(UpGiveSelector.select_dianpu)
        self.get_text1(UpGiveSelector.select_dianpu, test)

    def baobeilianjie(self, lianjie):
        print(u"输入宝贝链接：", lianjie)
        self.input_text(UpGiveSelector.input_baobeilianjie, lianjie)

    def baobeibiaoti(self, biaoti):
        print(u"输入宝贝标题：", biaoti)
        self.input_text(UpGiveSelector.input_baobeibiaoti, biaoti)

    def baobeizhutu(self, zhutu):
        print(u'上传主图！')
        self.input_text(UpGiveSelector.input_baobeizhutu, zhutu)

    def skutu(self, sku):
        print(u'上传sku图！')
        self.input_text(UpGiveSelector.input_skutu, sku)

    def zhanshijia(self, zhanshijia):
        print(u'输入展示价：', zhanshijia)
        self.input_text(UpGiveSelector.input_zhanshijia, zhanshijia)

    def chengjiaojia(self, chengjiaojia):
        print(u'输入成交价：', chengjiaojia)
        self.input_text(UpGiveSelector.input_chengjiaojia, chengjiaojia)

    def zhuyishixiang(self, zhuyishixiang):
        print(u'输入注意事项：', zhuyishixiang)
        self.input_text(UpGiveSelector.input_zhuyishixiang, zhuyishixiang)

    def btn_baobeixinxi(self):
        print(u'点击确认!')
        self.click(UpGiveSelector.btn_baobeixinxi)

    def tishi(self, test):
        print(u'判断提示语是否正确:')
        self.get_text1(UpGiveSelector.tip_tishi, test)

    # ------------------------------------分割线------------------------------------------------------


class UpGiveFind(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def shoujiban(self):
        print(u"点击手机版！")
        self.click(UpGiveSelector.btn_shoujiban)

    def diannaoban(self):
        print(u"点击电脑版！")
        self.click(UpGiveSelector.btn_diannaoban)

    def guanjianci(self):
        print(u"选择关键词！")
        self.click(UpGiveSelector.btn_guanjianci)

    def guanjianci1(self, guanjianci):
        print(u"输入关键词1：", guanjianci)
        self.input_text(UpGiveSelector.input_guanjianci1, guanjianci)

    def guanjianci2(self, guanjianci):
        print(u"输入关键词2：", guanjianci)
        self.input_text(UpGiveSelector.input_guanjianci2, guanjianci)

    def guanjianci3(self, guanjianci):
        print(u"输入关键词3：", guanjianci)
        self.input_text(UpGiveSelector.input_guanjianci3, guanjianci)

    def sousuopaixu(self):
        print(u"选择搜索排序！")
        self.click(UpGiveSelector.btn_sousuopaixu)

    def xiaoliang(self):
        print(u"选择 销量！")
        self.click(UpGiveSelector.select_xiaoliang)

    def zonghe(self):
        print(u"选择 综合！")
        self.click(UpGiveSelector.select_zonghe)

    def zhitongche(self):
        print(u"选择 直通车！")
        self.click(UpGiveSelector.select_zhitongche)

    # 关键词当前销量
    def dangqianxiaoliang1(self, xiaoliang):
        print(u'输入当前销量：', xiaoliang)
        self.input_text(UpGiveSelector.input_dangqianxiaoliang1, xiaoliang)

    # 关键词停留时间
    def tingliushijian1(self):
        print(u'点击停留时间！')
        self.click(UpGiveSelector.btn_tingliushijian1)

    # 关键词停留时间选择
    def fenzhong1_1(self):
        print(u'选择1-3分钟！')
        self.click(UpGiveSelector.select_fenzhong1_1)

    # 关键词付款时间
    def fukuanshijian1(self):
        print(u"点击加购付款时间！")
        self.click(UpGiveSelector.btn_fukuanshijian1)

    # 关键词付款时间选择
    def shijian1_1(self):
        print(u"选择6小时！")
        self.click(UpGiveSelector.select_shijian1_1)

    def taokouling(self):
        print(u'选择淘口令！')
        self.click(UpGiveSelector.btn_taokouling)

    def taokouling1(self, taokouling):
        print(u'输入淘口令：',taokouling)
        self.input_text(UpGiveSelector.input_taokouling, taokouling)

    def erweima(self):
        print(u'选择二维码！')
        self.click(UpGiveSelector.btn_erweima)

    def erweima1(self, erweima):
        print(u'上传二维码！',erweima)
        self.input_text(UpGiveSelector.input_erweima, erweima)

    # 淘口令 二维码当前销量
    def dangqianxiaoliang2(self, xiaoliang):
        print(u'输入当前销量：', xiaoliang)
        self.input_text(UpGiveSelector.input_dangqianxiaoliang2, xiaoliang)

    # 淘口令 二维码停留时间
    def tingliushijian2(self):
        print(u'点击停留时间！')
        self.click(UpGiveSelector.btn_tingliushijian2)

    # 淘口令 二维码选择停留时间
    def fenzhong2_1(self):
        print(u'选择1-3分钟！')
        self.click(UpGiveSelector.select_fenzhong2_1)

    # 淘口令 二维码付款时间
    def fukuanshijian2(self):
        print(u"点击加购付款时间！")
        self.click(UpGiveSelector.btn_fukuanshijian2)

    # 淘口令 二维码付款时间选择
    def shijian2_1(self):
        print(u"选择6小时！")
        self.click(UpGiveSelector.select_shijian2_1)



class UpGiveRelease(BasePage, unittest.TestCase):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def fabufenshu(self, fabufenshu):
        print(u"输入发布份数：", fabufenshu)
        self.input_text(UpGiveSelector.input_fabufenshu, fabufenshu)

    def paixiajianshu(self, paixiajianshu):
        print(u"输入拍下件数：", paixiajianshu)
        self.input_text(UpGiveSelector.input_paixiajianshu, paixiajianshu)

    def lijifabu(self):
        self.click(UpGiveSelector.btn_lijifabu)
