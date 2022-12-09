import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件内容
with open('三国演义.txt', 'r', encoding='utf-8') as f:
    text = f.read()
#读取停用词
with open('stopwords.txt', 'r', encoding='utf-8') as fs:
    stopwords = [line.strip() for line in fs]

# 使用 jieba 库进行中文分词
word_list = jieba.cut(text)

# 统计词频
word_freq = {}
for word in word_list:
    #跳过停用词
    if word not in stopwords:
        #跳过长度为一的单词
        if len(word) == 1:
            continue
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
merges = [('刘备',('玄德','玄德曰','玄德问','刘玄德','玄德大','玄德自','玄德闻','皇叔','刘皇叔')),
    ('关羽',('关公','云长','关云长')),
    ('孔明',('诸葛亮','孔明曰','孔明笑','孔明之','孔明自')),
    ('曹操',('丞相','孟德','曹公','曹孟德')),
    ('张飞',('翼德','张翼德')) ]

#合并单词
for merge in merges:
    for name in merge[1]:
        word_freq[merge[0]] += word_freq.get(name, 0)
        del word_freq[name]

# 生成词云
wordcloud = WordCloud(
    #设置背景为白色
    background_color='white',
    #设置大小，提高清晰度
    scale=32,
    #设置显示数量
    max_words=200,
    #设置字体
    font_path='./simhei.ttf')
#转换为image并显示
wordcloud.generate_from_frequencies(word_freq).to_image().show()
