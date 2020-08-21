import unittest
import time
import HTMLTestRunner
casedir = "C:\\Users\\Administrator\\PycharmProjects\\untitled\\Test"
tests = unittest.defaultTestLoader.discover(casedir, "test_1.py")

# file = "C:\\Users\\Administrator\\PycharmProjects\\untitled\\report\\reportreport{}
# .txt".format(time.strftime("%Y%m%d%H%M%S"),time.localtime())
# with open(file,"w") as txtfile:
#     runner = unittest.TextTestRunner(stream=txtfile,verbosity=2)
#     runner.run(tests)

reporthtml = "C:\\Users\\Administrator\\PycharmProjects\\untitled\\report\\reportreport{}.html"\
    .format(time.strftime("%Y%m%d%H%M%S"), time.localtime())
with open(reporthtml, "wb+") as htmlfile:
    runner = HTMLTestRunner.HTMLTestRunner(stream=htmlfile, title="测试报告", description="用例执行情况")
    runner.run(tests)
