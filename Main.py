from spider.ReSpider import JobRe
from analysis.cloud import get_cloud


class Main:
    @staticmethod
    def run(key):

        print("开始爬取")
        JobRe().crawl(key)
        print("爬取数据完毕")

        print("开始抽取关键字, 生成抽取结果, 并生成词云")
        get_cloud(key)

        # print("开始发送结果报告")
        # send_mail(key, "807705073@qq.com")
        # send_mail(key, "nilezhou123@gmail.com")


if __name__ == "__main__":
    # keys = ["电气设备装配", "电气维修技师", "自动化设备装调维修工","自动化企业技术总监","自动化生产线维护技术员",
    #         "自动化系统工程师","自动化系统助工程师","自动化系统总工程师设计师","电气自动化仪表安装员",
    #         "电气仪表自控工程师"]
    # for key in keys:
    #     Main.run(key)
    Main.run("python工程师")

