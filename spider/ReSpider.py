import re
import time
from spider.Spider import Spider
from urllib import parse

class JobRe(Spider):
    def __init__(self):
        super(JobRe, self).__init__()

    def parse_job_list(self, text):
        try:
            pattern = re.compile('<div class="job-info">.*?<h3.*?title="(.*?)">.*?<a href="(.*?)".*?title="(.*?)">.*?'
                                 '<p class="company-name">.*?>(.*?)</a>.*?<p class="field-financing">.*?target="_blank">'
                                 '(.*?)</a>.*?</span>', re.S)
            datas = re.findall(pattern, text)
            for data in datas:
                title = data[0] # 招聘标题
                href = data[1] # 详细页面的url
                result = data[2].split('_')
                salary = result[0] # 薪水
                region = result[1] # 地区
                degree = result[2] # 学历要求
                exper = result[3] # 工作经验要求
                company = data[3] # 公司名
                industry = data[4] # 行业名

                print("入口解析到一条职位信息: ", data)

                # 进去获取详细信息
                detail = self.request_job_details(parse.urljoin('https://www.liepin.com', href))
                self.append(title, salary, region, degree, exper, company, industry, detail)

                time.sleep(2)

        except Exception as e:
            print("re parse_job_list error : ", str(e))



    def parse_job_details(self, s):
        try:
            pattern = re.compile(
                '<div class="content content-word">(.*?)</div>.*?<div class="job-item main.*?">', re.S)
            text = re.search(pattern, s)
            if not text:
                p2 = re.compile('<div class="job-info-content">(.*?)</div>', re.S)
                text = re.search(p2, s)

            # re.S代表把\n看成普通字符, '.' 是匹配除了'\n'以外的任意字符
            detail = re.sub(re.compile('[<br(/)?>\r\t\n]', re.S), '', text.group(1))  # re.sub()替换
            print(detail)
            if detail:
                return detail
            else:
                self.job_data.append("暂无职位信息")
            self.count += 1

            print("crawel ", self.count, "条数据")
        except Exception as e:
            print("正则匹配详细信息出错 : ", str(e))



