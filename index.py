import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件内容
with open('三国演义.txt', 'r', encoding='utf-8') as f:
    text = f.read()

with open('stopwords.txt', 'r', encoding='utf-8') as fs:
    stopwords = [line.strip() for line in fs]

# 使用 jieba 库进行中文分词
word_list = jieba.cut(text)

# 统计词频
word_freq = {}
for word in word_list:
    if word not in stopwords:
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

for merge in merges:
    for name in merge[1]:
        word_freq[merge[0]] += word_freq.get(name, 0)
        del word_freq[name]

# 生成词云
wordcloud = WordCloud(
    background_color='white',
    scale=32,
    max_words=200,
    font_path='./simhei.ttf')
wordcloud.generate_from_frequencies(word_freq).to_image().show()

# # 显示词云图
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
