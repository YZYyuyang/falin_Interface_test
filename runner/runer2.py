from testcase_read.testcase_read1 import *
data1 = Testcase().test02()
osVersion = "1"
apiVersion = "1.0.0"
platform = "huawei"
stream = open("..\data\yaml.yaml", mode='r', encoding="utf-8")
url = yaml.load(stream)["Url"]["url1"]
i = 1

import unittest,os
from ddt import ddt,data,unpack,file_data

@ddt
class Testwork(unittest.TestCase):
    @data(*data1)
    @unpack
    def test_01(self, num,url, data, port):
        url1 = "http://testapi.imlaw.cn/"+ url
        if port == "客户端":
            e = Encryption3()
            result = e.app_aes_data(data)
            print('加密结果>>>', result)
            data ={"data": result}
            m = MultipartEncoder(data)
            sign = e.app_aes_sign(data)
            header = {"sign":sign,"osVersion":osVersion,"apiVersion": apiVersion,"platform": platform}
            result1 = requests.post(url1, data=data,headers = header,
                 verify=False, timeout=10)
            print(f"接口相应内容为%s"%result1.text)
            print(f"接口相应状态码为%s"%result1.status_code)
            ExcelDeal.write_cell_by_row_and_col(sheetname = "Sheet1",row = num+1,col = 6,data = result1.text)
            ExcelDeal.write_cell_by_row_and_col(sheetname="Sheet1", row=num + 1, col=7, data=result1.status_code)
        elif port =="管理端":
            e = Encryption3()
            cms_result = e.cms_sign(data = data1)
            # cms_result = e.cms_encrypt(data3)
            print('管理端加密结果>>>', cms_result)
            result1 = requests.post(url1, data=cms_result,
                                    verify=False, timeout=10)
            print(f"result1为%s" % result1)
            ExcelDeal.write_cell_by_row_and_col(sheetname="Sheet1", row=num + 1, col=6, data=result1.text)
            ExcelDeal.write_cell_by_row_and_col(sheetname="Sheet1", row=num+ 1, col=7, data=result1.status_code)

if __name__ == "__main__":
    unittest.main()