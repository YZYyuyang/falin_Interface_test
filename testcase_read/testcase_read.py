import requests,unittest
# from apitest.data_fetch.exceldeal import *
# from apitest.encryption_algorithm.sign_data_encryption import *

from data_fetch.exceldeal import *
from encryption_algorithm.sign_data_encryption import *
from requests_toolbelt import MultipartEncoder
ExcelDeal = ExcelDeal()

class Test_HLTestCase(unittest.TestCase):

    def setup(self):
        self.cols = ExcelDeal.get_rows("Sheet1")   #行数
        print(self.cols)
        self.osVersion = "1"
        self.apiVersion = "1.0.0"
        self.platform = "huawei"
        stream = open("..\data\yaml.yaml", mode='r', encoding="utf-8")
        self.url = yaml.load(stream)["Url"]["url1"]

    def test_api_test_001(self):
        a = 1
        b = 2
        c = a + b
        print(c)
        return c

    def test_api_test_002(self):
        for i in range(self.cols):
            url1 = ExcelDeal.get_cell_by_row_and_col(sheetname = "Sheet1",row = i+1,col = 2)
            url1 = self.url + url1         #网址的拼接
            data1 = ExcelDeal.get_cell_by_row_and_col(sheetname = "Sheet1",row = i+1,col = 3)
            port = ExcelDeal.get_cell_by_row_and_col(sheetname = "Sheet1",row = i+1,col = 4)
            if port =="客户端":
                e = Encryption3()
                result = e.app_aes_data(data1)
                print('加密结果>>>', result)
                data ={"data": result}
                m = MultipartEncoder(data)
                sign = e.app_aes_sign(data1)
                header = {"sign":sign,"osVersion":self.osVersion,"apiVersion": self.apiVersion,"platform": self.platform}
                result1 = requests.post(url1, data=data,headers = header,
                     verify=False, timeout=10)
                ExcelDeal.write_cell_by_row_and_col(sheetname = "Sheet1",row = i+1,col = 5,data = result1.text)
                ExcelDeal.write_cell_by_row_and_col(sheetname="Sheet1", row=i + 1, col=6, data=result1.status_code)
            elif port =="管理端":
                e = Encryption3()
                cms_result = e.cms_sign(data = data1)
                # cms_result = e.cms_encrypt(data3)
                print('管理端加密结果>>>', cms_result)
                result1 = requests.post(url1, data=cms_result,
                                        verify=False, timeout=10)
                print(f"result1为%s" % result1)
                ExcelDeal.write_cell_by_row_and_col(sheetname="Sheet1", row=i + 1, col=5, data=result1.text)
                ExcelDeal.write_cell_by_row_and_col(sheetname="Sheet1", row=i + 1, col=6, data=result1.status_code)


    def tearDown(self):
        pass


# if __name__ == '__main__':
#     testcase = Test_HLTestCase()
#     testcase.test_api_test_001()
