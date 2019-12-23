import jieba.posseg as pseg
import re

"""
    获取词性dict与词计数
"""


def get_skills(df):
    words = {}
    cnts = {}
    pattern = re.compile("[岗位|任职]{2}要求(.*)")
    for line in df["detail"]:
        if not isinstance(line, float):  # 不为nan
            for find in re.findall(pattern, line):
                segs = pseg.cut(find)
                for seg in segs:
                    word = seg.word.lower()
                    if not word in words:
                        words[word] = seg.flag
                        cnts[word] = 1
                    else:
                        cnts[word] += 1

    return words, cnts


"""
    排除一些词与特殊字符, 只取特定词性
"""


def filt(d, pos_list):
    no = ["职责", "idea", "专业", "方面", "理", '大学本科', "万行",
          "研发部门", "流利", "问题", "计算机", "机器", "学习",
          "技术", "原理", "人才", "代码", "本科", "工具", "思维", "公司",
          "工程", "员工", "岗位", "体系", "解决问题", "语言", "互联网", "大",
          "实际", "方向", "重点", "原创", "大", "习惯", "we", "专业本科", "and", "能力"]
    res = []
    for k, v in d.items():
        if v in pos_list and k not in no and not k.isdigit():
            res.append(k)
    return res


"""
    获取筛选后的降序词典
"""


def get_filted_cnts(filted_words, cnts):
    d = {}
    for word in filted_words:
        d[word] = cnts[word]
    return dict(sorted(d.items(), key=lambda e: e[1], reverse=True))  # sort为list
