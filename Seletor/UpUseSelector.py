from selenium.webdriver.common.by import By


class UpUseSelector:

    # 线上模式产品赠送宝贝信息---------------------------------------------------------------------

    btn_fabushiyong = (By.XPATH, '//*[@id="content"]/nav/a[2]/p')     # 发布试用

    btn_xianshangmoshi = (By.XPATH, '//*[@id="release"]/div[1]/ul/li[1]')  # 线上模式

    btn_shiyongleixing = (By.XPATH, '//*[@id="good_info"]/div[2]/div/div[1]/div[1]/div/input')  # 试用类型
    select_chanpingzengsong = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')   # 产品赠送

    btn_suoshudianpu = (By.XPATH, '//*[@id="good_info"]/div[2]/div/div[2]/div[1]/div/input')  # 所属店铺
    select_dianpu = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')   # 第一间铺
    select_dianpu2 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')  # 第二间铺

    input_baobeilianjie = (By.CSS_SELECTOR, '#good_info > div.form > div > div:nth-child(3) > input[type=text]')
    # 宝贝链接

    input_baobeibiaoti = (By.CSS_SELECTOR, '#good_info > div.form > div > div:nth-child(4) > input[type=text]')   # 宝贝标题

    input_baobeizhutu = (By.XPATH, '//*[@id="imgUpload"]/div/input')   # 宝贝主图

    input_skutu = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[5]/div[2]/div/div/input')
    # SKU图

    input_zhanshijia = (By.CSS_SELECTOR, '#good_info > div.form > div > div.form_item_money > div:nth-child(1) > input[type=text]')  # 展示价
    input_chengjiaojia = (By.CSS_SELECTOR, '#good_info > div.form > div > div.form_item_money > div:nth-child(2) > input[type=text]')  # 成交价

    input_zhuyishixiang = (By.CSS_SELECTOR, '#good_info > div.form > div > div:nth-child(7) > textarea')  # 注意事项

    btn_baobeixinxi = (By.CSS_SELECTOR, '#good_info > div.form > div > input')  # 确认按钮

    tip_tishi = (By.CLASS_NAME, 'el-message__content')   # 提示框

    box = (By.CLASS_NAME, 'el-checkbox')  # 复选框


class SousuoPage1():

    # 搜索信息------------------------------------------------------------------------
    # 关键词页
    btn_shoujiban = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(1) > ul > li.active')   # 手机版
    btn_diannaoban = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(1) > ul > li:nth-child(2)')   # 电脑版

    btn_guanjianci = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(2) > div > label.el-radio.is-checked > span.el-radio__label')  # 关键词爸爸
    input_guanjianci1 = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(4) > div.input_list > input[type=text]:nth-child(1)')   # 关键词1
    input_guanjianci2 = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(4) > div.input_list > input[type=text]:nth-child(2)')  # 关键词2
    input_guanjianci3 = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(4) > div.input_list > input[type=text]:nth-child(3)')  # 关键词3

    btn_sousuopaixu = (By.XPATH, '//*[@id="search_info"]/div[2]/div/div[4]/div/div/input')    # 搜索排序
    select_xiaoliang = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')   # 销量
    select_zonghe = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]')  # 综合
    select_zhitongche = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[3]')  # 直通车

    input_xiaoliang = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(6) > input[type=text]')  # 当前销量

    btn_tingliushijian = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(8) > div > div > input')
    # 停留时间
    select_fenzhong = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]')    # 1-3分钟

    btn_fukuanshijian = (By.CSS_SELECTOR, '#search_info > div.form > div > div.form_item.paytime > div > div > input')
    # 加购付款时间
    select_shijian1 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]')   # 6小时


class SousuoPage2():

    # 搜索信息----------------------------------------------------------------------------------------
    # 淘口令 + 二维码
    btn_taokouling = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(2) > div > '
                                       'label:nth-child(2) > span.el-radio__label')   # 淘口令
    btn_erweima = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(2) > div > '
                                    'label:nth-child(3) > span.el-radio__label')  # 二维码

    input_taokouling = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(4) > input')   # 输入淘口令
    input_erweima = (By.CSS_SELECTOR, '#imgUpload > div > input[type=file]')  # 上传二维码

    input_xiaoliang = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(5) > input[type=text]')  # 销量

    btn_tingliushijian = (By.CSS_SELECTOR, '#search_info > div.form > div > div:nth-child(7) > div > div > input')  # 停留时间
    select_fenzhong = (By.CSS_SELECTOR, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')  # 1-3分钟

    btn_fukuanshijian = (By.CSS_SELECTOR, '#search_info > div.form > div > div.form_item.paytime > div > div > input')
    # 加购付款时间

    select_shijian1 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]')  # 6小时


class FabuPage():

    input_fabufenshu = (By.CSS_SELECTOR, '#timing > div.form > div > div.form_item_two > '
                                         'div:nth-child(1) > input[type=text]')   # 发布份数
    input_paixiajianshu = (By.CSS_SELECTOR, '#timing > div.form > div > div.form_item_two > '
                                            'div:nth-child(2) > input[type=text]')  # 拍下件数

    box_jietu1 = (By.CSS_SELECTOR, '#timing > div.form > div > div:nth-child(3) > div.el-checkbox-group '
                                   '> div > label:nth-child(1) > span.el-checkbox__label')
    box_jietu2 = (By.CSS_SELECTOR, '#timing > div.form > div > div:nth-child(3) > div.el-checkbox-group '
                                   '> div > label:nth-child(2) > span.el-checkbox__label')
    box_jietu3 = (By.CSS_SELECTOR, '#timing > div.form > div > div:nth-child(3) > div.el-checkbox-group '
                                   '> div > label:nth-child(3) > span.el-checkbox__label')
    box_jietu4 = (By.CSS_SELECTOR, '#timing > div.form > div > div:nth-child(3) > div.el-checkbox-group '
                                   '> div > label:nth-child(4) > span.el-checkbox__label')

    btn_lijifabu = (By.CSS_SELECTOR, '#release > div.lastStep > input:nth-child(3)')   # 立即发布
