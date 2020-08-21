from selenium.webdriver.common.by import By


class DownGiveSelector:
    btn_fabushiyong = (By.XPATH, '//*[@id="content"]/nav/a[2]/p')  # 发布试用
    btn_xianxiamoshi = (By.XPATH, '//*[@id="release"]/div[1]/ul/li[2]')  # 线下模式
    btn_shiyongleixing = (By.XPATH, '//*[@id="good_info"]/div[2]/div/div[1]/div[1]/div/input')  # 试用类型
    select_chanpinzengsong = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')  # 产品赠送
    input_chanpinname = (By.XPATH, '//*[@id="good_info"]/div[2]/div/div[2]/input')  # 产品名称
    input_chanpinzhutu = (By.XPATH, '//*[@id="imgUpload"]/div/input')  # 产品主图
    input_chanpinjiage = (By.XPATH, '//*[@id="good_info"]/div[2]/div/div[4]/div/input')  # 产品价格
    input_fabufenshu = (By.XPATH, '//*[@id="good_info"]/div[2]/div/div[5]/div/input')  # 发布份数
    btn_lijifabu = (By.CSS_SELECTOR, '#release > div.lastStep > input')  # 立即发布
