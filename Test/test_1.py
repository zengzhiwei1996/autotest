import unittest
import time
from selenium import webdriver
from Page.UpGivePage import UpGiveBabyMes
from Page.UpGivePage import UpGiveFind
from Page.UpGivePage import UpGiveRelease

from Page.DownGivePage import DownGiveBabyMes

from Seletor.UpGiveSelector import UpGiveSelector
from Case.Test_Judge import Fabu_judge
from Case.Test_Judge import Tishi_judge

from Case.Login_Case import LoginCase


class Test(unittest.TestCase):

    # 不读取本地缓存
    # def setUp(self):
    # self.driver = webdriver.Chrome(r'D:\ZZW\chromedriver_win32\chromedriver.exe')
    # self.driver.get("http://192.168.0.181:3008")
    # self.driver.maximize_window()

    # 读取本地缓存
    @classmethod
    def setUpClass(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
        self.driver = webdriver.Chrome(r'D:\ZZW\chromedriver_win32\chromedriver.exe', 0, self.option)
        self.driver.get("http://192.168.0.181:3008")
        self.driver.maximize_window()

    # 线上模式产品赠送
    def test_1(self):
        driver = self.driver

        # Login_page = Login_Page(driver)

        # Login_page.input_zhanghao(LoginCase.name)
        # Login_page.input_mima(LoginCase.password)
        # time.sleep(5)

        # Login_page.btn_denglu()
        # time.sleep(3)

        # Login_page.btn_queren()

        # Login_page.btn_zhidao()
        # time.sleep(2)

        print(u"-----------------------宝贝信息填写-------------------------------")

        UpGiveBabyMes_Page = UpGiveBabyMes(driver)

        UpGiveBabyMes_Page.fabushiyong()          # 发布试用
        time.sleep(2)
        UpGiveBabyMes_Page.xianshangmoshi()       # 线上模式
        time.sleep(2)

        UpGiveBabyMes_Page.shiyongleixing()   # 试用类型选择
        time.sleep(2)
        UpGiveBabyMes_Page.chanpinzengsong(Fabu_judge.test1)  # 产品赠送
        time.sleep(2)

        # Fabu_Page.chanpingshiyong(Fabu_judge.test2)  # 产品试用
        # time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test1)

        UpGiveBabyMes_Page.suoshudianpu()   # 选择所属店铺
        time.sleep(2)
        UpGiveBabyMes_Page.dianpu(Fabu_judge.test3)   # 第一间铺
        time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test2)

        UpGiveBabyMes_Page.baobeilianjie(LoginCase.lianjie)  # 宝贝链接
        time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test3)

        UpGiveBabyMes_Page.baobeibiaoti(LoginCase.biaoti)  # 宝贝标题
        time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test4)

        UpGiveBabyMes_Page.baobeizhutu(LoginCase.zhutu)   # 上传主图
        time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test5)

        UpGiveBabyMes_Page.skutu(LoginCase.zhutu)        # 上传sku图
        time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test5)

        UpGiveBabyMes_Page.zhanshijia(LoginCase.chengjiaojia)   # 展示价
        time.sleep(2)

        # 点击宝贝信息确认判断
        UpGiveBabyMes_Page.btn_baobeixinxi()
        time.sleep(2)
        UpGiveBabyMes_Page.tishi(Tishi_judge.test6)

        UpGiveBabyMes_Page.chengjiaojia(LoginCase.chengjiaojia)   # 成交价
        time.sleep(2)
        UpGiveBabyMes_Page.zhuyishixiang(LoginCase.zhuyishixiang)   # 注意事项
        time.sleep(2)
        UpGiveBabyMes_Page.btn_baobeixinxi()    # 确认
        time.sleep(2)

        print(u"-----------------------宝贝信息结束-------------------------------")
        print(u"-----------------------搜索信息-----------------------------------")

        UpGiveFind_Page = UpGiveFind(driver)

        UpGiveFind_Page.shoujiban()   # 手机版
        time.sleep(1)
        UpGiveFind_Page.guanjianci()  # 关键词爸爸
        time.sleep(2)

        UpGiveFind_Page.guanjianci1(LoginCase.guanjianci1)    # 关键词1
        time.sleep(1)
        UpGiveFind_Page.guanjianci2(LoginCase.guanjianci2)    # 关键词2
        time.sleep(1)
        UpGiveFind_Page.guanjianci3(LoginCase.guanjianci3)    # 关键词3
        time.sleep(1)

        UpGiveFind_Page.sousuopaixu()   # 搜索排序
        time.sleep(1)
        UpGiveFind_Page.xiaoliang()   # 选择销量
        time.sleep(1)

        UpGiveFind_Page.dangqianxiaoliang1(LoginCase.dangqianxiaoliang)    # 输入当前销量
        time.sleep(1)

        # 附加项复选框
        box = driver.find_elements(*UpGiveSelector.box)
        box[1].click()    # 问大家
        box[2].click()    # 货比三家

        UpGiveFind_Page.fukuanshijian1()   # 付款时间
        time.sleep(2)
        UpGiveFind_Page.shijian1_1()   # 选择6小时
        time.sleep(2)

        box[4].click()
        box[7].click()
        box[8].click()

        time.sleep(2)

        print(u"-----------------------搜索信息结束-------------------------------")

        print(u"-----------------------填写发布信息-------------------------------")
        UpGiveRelease_Page = UpGiveRelease(driver)
        UpGiveRelease_Page.fabufenshu(LoginCase.fabufenshu)    # 发布份数
        UpGiveRelease_Page.paixiajianshu(LoginCase.paixiajianshu)    # 拍下件数
        time.sleep(1)
        UpGiveRelease_Page.lijifabu()      # 立即发布按钮
        time.sleep(20)
        print(u"-----------------------发布信息结束-------------------------------")

        driver.close()


    def test_2(self):
        driver = self.driver
        DownGiveBabyMes_Page = DownGiveBabyMes(driver)
        DownGiveBabyMes_Page.fabushiyong()
        time.sleep(2)
        DownGiveBabyMes_Page.xianxiamoshi()
        time.sleep(2)
        DownGiveBabyMes_Page.shiyongleixing()
        time.sleep(2)
        DownGiveBabyMes_Page.chanpinzengsong(Fabu_judge.test1)
        time.sleep(2)
        DownGiveBabyMes_Page.chanpinmingcheng("zzw602-1")
        time.sleep(2)
        DownGiveBabyMes_Page.baobeizhutu(LoginCase.zhutu)  # 上传主图
        time.sleep(2)
        DownGiveBabyMes_Page.chanpinjiage(5)
        time.sleep(2)
        DownGiveBabyMes_Page.fabufenshu(9)
        time.sleep(2)
        DownGiveBabyMes_Page.btn_lijifabu()
        time.sleep(2)
        driver.close()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

    # testunit = unittest.TestSuite
    # testunit.addTest(Test("test_1"))

    # pytest.main(['-s','test.py','--html=./zzw.html'])
