from selenium.webdriver.common.by import By


class Login:
    input_zhanghao = (By.XPATH, '//*[@id="formBox"]/div/div[2]/input')  # 账号
    input_mima = (By.XPATH, '//*[@id="formBox"]/div/div[3]/input')      # 密码
    btn_denglu = (By.XPATH, '//*[@id="formBox"]/div/input')           # 登录按钮
    btn_queren = (By.XPATH, '//*[@id="alert"]/div/div/input')         # 确认按钮
    btn_zhidao = (By.XPATH, '//*[@id="home"]/div[3]/div/div/img[3]')  # 知道了按钮
