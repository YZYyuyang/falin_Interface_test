# -*- coding:utf-8 -*-
from unittestreport import TestRunner
import requests,unittest,time,os
import hashlib,ast,ddt
# from apitest.data_fetch.exceldeal import *
# from apitest.encryption_algorithm.sign_data_encryption import *
from data_fetch.exceldeal import *
from encryption_algorithm.sign_data_encryption import *
from requests_toolbelt import MultipartEncoder
ExcelDeal = ExcelDeal()



class Testcase():
    def __init__(self):
        self.cols = ExcelDeal.get_rows("Sheet1")   #行数
        print(self.cols)
        self.osVersion = "1"
        self.apiVersion = "1.0.0"
        self.platform = "huawei"
        stream = open("..\data\yaml.yaml", mode='r', encoding="utf-8")
        try:
            self.url = yaml.load(stream)["Url"]["url1"]
        except:
            pass

    def api_test(self):
        all_num = ExcelDeal.get_cols_by_name_y(sheetname="Sheet1", y=0)              # 字典
        all_url1 = ExcelDeal.get_cols_by_name_y(sheetname = "Sheet1",y = 2)         #字典
        all_data1 = ExcelDeal.get_cols_by_name_y(sheetname = "Sheet1",y=3)
        all_port = ExcelDeal.get_cols_by_name_y(sheetname = "Sheet1",y=4)
        return all_num,all_url1,all_data1,all_port          #返回元祖

    def test02(self):
        q = self.api_test()
        list2 = []
        for i in range(len(q[0])-1):
            list1 = []
            list1.append(q[0][i+1])
            list1.append(q[1][i + 1])
            list1.append(q[2][i + 1])
            list1.append(q[3][i + 1])
            list2.append(list1)
        return list2

    def test03(self):
        pass

if __name__ == "__main__":
    testcase = Testcase()
    testcase.test02()