import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_file = os.path.join(prj_path, 'data', 'test_user_data.xlsx')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_passwd = '123456'
db = 'api_test'

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '791160580@qq.com'
smtp_password = 'orpemfbxtbnvbbeg'

sender = smtp_user  # 发件人
receiver = 'zhizhong.li@midea.com'  # 收件人
subject = '接口测试报告'  # 邮件主题
