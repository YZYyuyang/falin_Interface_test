# -*- coding:utf-8 -*-
from unittestreport import TestRunner
import requests,unittest,time,os,ddt
import hashlib,ast
# from apitest.data_fetch.exceldeal import *
# from apitest.encryption_algorithm.sign_data_encryption import *
from data_fetch.exceldeal import *
from encryption_algorithm.sign_data_encryption import *
from requests_toolbelt import MultipartEncoder
# ExcelDeal = ExcelDeal()
print()

def AutoRun(TestCaseName):
    TestCase_path = "E:\\法律1-1接口测试\\apitest\\runner"
    discover = unittest.defaultTestLoader.discover(
        TestCase_path, pattern=TestCaseName, top_level_dir=None)
    report_path = "E:\\法律1-1接口测试\\apitest\\data"
    report_title = "MyReport"
    report_name = report_title + time.strftime('%H-%M-%S')
    runner = TestRunner(suite = discover,filename= report_name + ".html",report_dir=report_path,title='测试报告',tester='段欣',desc="华律PC站测试的报告",templates=2)
    runner.run()

if __name__ == "__main__":
    AutoRun("*2.py")