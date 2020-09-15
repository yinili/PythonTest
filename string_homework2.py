'''
小易喜欢的单词具有以下特性：
1、单词每个字母都是大写字母
2、单词没有连续相等的字母

例如：
小易不喜欢"ABBA"，因为有两个连续的B
小易喜欢"A"，"ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词
'''

word = input('请输入单词：')

for i in range(len(word)):
    if word[i]<'A' or word[i]>'Z':
        print('不喜欢！不是大写字母')
        break
    else:
        if i < len(word)-1 and word[i] == word[i+1]:
            print('不喜欢！出现了叠词')
            break
else:
    print('喜欢')
