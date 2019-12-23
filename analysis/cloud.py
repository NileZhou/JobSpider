import pandas as pd
import wordcloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from .key_word import get_skills
from .key_word import filt
from .key_word import get_filted_cnts
from os import sep


def get_cloud(job):
    data_dir = "data"+sep
    print("get_cloud: ", job)
    df = pd.read_csv(data_dir + job + "_res.csv", engine="python", encoding="utf_8_sig") # engine默认为c engine, 不支持文件名含有中文
    words, cnts = get_skills(df)
    filted_words = filt(words, ["n", "eng", "nz"])
    filt_cnt = get_filted_cnts(filted_words, cnts)

    with open(data_dir + job + "_key_skills.txt", "w", encoding="utf-8") as f:
        for k, v in filt_cnt.items():
            f.write(k+"="+str(v)+"\n")

    apple_mask = np.array(Image.open(data_dir+"apple2.jpg"))

    wc = wordcloud.WordCloud(font_path=data_dir+"NotoSansCJKsc-DemiLight.otf",
                             background_color="white",  # 背景颜色
                             max_words=400,  # 词云显示的最大词数
                             mask=apple_mask,  # 设置背景图片
                             max_font_size=200,  # 字体最大值
                             min_font_size=40,
                             random_state=42,
                             margin=1
                             )
    image_colors = wordcloud.ImageColorGenerator(apple_mask)
    if len(filt_cnt):
        wc.generate_from_frequencies(filt_cnt)
        # show
        plt.figure(figsize=[20, 20])
        plt.tight_layout(pad=0)
        plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")

        plt.savefig(data_dir+job+"_cloud.png")
        print("生成词云完毕")