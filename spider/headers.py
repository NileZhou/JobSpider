from spider.agents import get_random_agent

headers = {
                'Referer': 'https://www.liepin.com/zhaopin/?d_sfrom=search_fp_nvbar&init=1',
                "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.8",
                'Cache-Control': 'max-age=0',
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests" : "1",
                'User-Agent': get_random_agent()
}

def get_headers():
    return headers


