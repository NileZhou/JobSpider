import abc
import requests
from spider.headers import get_headers
from os import sep


class Spider():
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.row_title = ['title', 'salary', 'region', 'degree', 'exper', 'company', 'industry', 'detail']
        self.job_data = []
        self.count = 0

    """
        爬虫入口
    """
    def crawl(self, key):
        print("crawl: ", key)
        url = "https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&key=" + key
        self.key = key
        self.request_job_list(url)

        self.save()


    """
        获取并解析职位信息
    """
    def request_job_list(self, url):
        try:
            headers = get_headers()
            reponse = requests.get(url, headers=headers)
            if reponse.status_code != 200: return
            self.parse_job_list(reponse.text)
        except Exception as e:
            print('request_job_list error : {}'.format(e))

    """
        解析职位URL
    """
    @abc.abstractmethod
    def parse_job_list(self, text):
        pass

    """
        请求职位详细页面
    """
    def request_job_details(self, url):
        try:
            print("解析到的子url: ", url)
            headers = get_headers()
            response = requests.get(url, headers=headers)
            if response.status_code != 200: return
            return self.parse_job_details(response.text)
        except Exception as e:
            # raise e
            print('向职位详细界面发起请求错误 : {}'.format(e))


    """
        解析职位详细页面
    """
    @abc.abstractmethod
    def parse_job_details(self, text):
        pass

    def append(self, title, salary, region, degree, exper, company, industry, detail):
        self.job_data.append([title, salary, region, degree, exper, company, industry, detail])


    def data_clear(self):
        self.job_data = []

    def extract(self, data):
        return data[0] if len(data) > 0 else ""


    def get_data(self):
        return self.job_data


    def save(self):
        titles = []
        salarys = []
        regions = []
        degrees = []
        expers = []
        companys = []
        industrys = []
        details = []
        for line in self.job_data:
            titles.append(line[0])
            salarys.append(line[1])
            regions.append(line[2])
            degrees.append(line[3])
            expers.append(line[4])
            companys.append(line[5])
            industrys.append(line[6])
            details.append(line[7])

        import pandas as pd

        df = pd.DataFrame()
        df["title"] = titles
        df['salary'] = salarys
        df["region"] = regions
        df["degree"] = degrees
        df["exper"] = expers
        df["company"] = companys
        df["industry"] = industrys
        df["detail"] = details

        df.to_csv("data"+sep+self.key+"_res.csv", encoding='utf_8_sig', index=False)


