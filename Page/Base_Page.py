class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 输入填写
    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    # 点击
    def click(self, loc):
        self.find_element(*loc).click()

    # 获得描述
    def get_text(self, loc):
        return self.find_element(*loc).text

    # 获得描述且断言
    def get_text1(self, loc, test):
        text = self.find_element(*loc).text
        print("描述为：", text)
        test = test
        try:
            self.assertIn(test, text)
            print("与 ", test, " 一致")
        except AssertionError as e:
            print("与 ", test, " 不一致")

    # 获得网页标题
    def get_title(self):
        return self.driver.title
