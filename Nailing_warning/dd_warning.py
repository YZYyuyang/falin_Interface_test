from WorkWeixinRobot.work_weixin_robot import WWXRobot
import requests,base64,hashlib

class WXWork_SMS():

    def WXWork_txt(self,content):
        wwx = WWXRobot(key='38ba4b23-22ad-4961-8886-9a364d489cac')
        wwx.send_text(content=content)

    # Markdown类型消息
    def send_msg_markdown(self,case_name,case_code_name,case_log_msg):
        """

        :param case_name: 用例英文名称
        :param case_code_name: 用例编号
        :param case_log_msg: 用例报错信息
        :return:
        """

        headers = {"Content-Type" : "text/plain"}
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=38ba4b23-22ad-4961-8886-9a364d489cac"
        send_data = {
            "msgtype": "markdown",  # 消息类型，此时固定为markdown
            "markdown": {
                "content": "# **提醒！UI自动化测试用例错误反馈**<font color=\"warning\"></font>\n" +  # 标题 （支持1至6级标题，注意#与文字中间要有空格）
                           "#### **请相关同事注意问题，及时跟进！**\n" +  # 加粗：**需要加粗的字**
                           "> 问题用例名称：<font color=\"info\">%s</font> \n"%case_name +  # 引用：> 需要引用的文字
                           "> 测试用例代码编号：<font color=\"warning\">%s</font> \n"%case_code_name +  # 字体颜色(只支持3种内置颜色)
                           "> 问题用例日志信息：<font color=\"warning\"> %s </font>"%case_log_msg    # 绿色：info、灰色：comment、橙红：warning
            }
        }
        res = requests.post(url = send_url, headers = headers, json = send_data)
        print(res)

    def send_mpng_markdown(self,pngfile):
        # 图片base64码
        with open(pngfile,"rb") as f:
            base64_data = base64.b64encode(f.read())
            base64_data = str(base64_data, 'utf-8')
        file = open(pngfile, "rb")
        md = hashlib.md5()
        md.update(file.read())
        res1 = md.hexdigest()
        url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=38ba4b23-22ad-4961-8886-9a364d489cac"
        headers = {"Content-Type": "text/plain"}
        data = {
            "msgtype": "image",
            "image": {
                "base64": base64_data,
                "md5": res1
            }
        }
        r = requests.post(url, headers=headers, json=data)
        print(r.text)
