# https://lovit.github.io/archives/#/page2

'''
주요사업
목적사업
주요제품
주요사업의 내용
당사가 생산하는
당사가 납품하는
향후 추진 사업
당사는
영위할
공급해 오고
공급하고

1. 기업보고서(xml) 에서 문단 p 태그 기준으로 태깅하고
2. 문단별로 문장조합

3. 상위 키워드 기준으로 내용검색하여
4. 키워드 조건 만족하는 문단 발견 시 키워드 분석 대상에 포함

'''



from collections import Counter
from konlpy.tag import Komoran
from konlpy.tag import Kkma
from konlpy.tag import Twitter


komoran = Komoran()

def main():
    wd_1 = set('가족같은')
    wd_2 = set('가족')

    wd3 = wd_1 & wd_2
    print(wd3)


def tokenized(src):

    sent = ''
    li = []
    cnt = 0
    sent_len = len(src)
    for wd in src:

        if wd != ' ' and wd != '(' and wd != ')':
            sent += wd
            if  sent_len-1 <= cnt:
                li.append(sent)
        else:
            li.append(sent)
            sent = ''
        cnt += 1


    for wd in li:
        print(wd)


def str_cmp(cmp, src):
    ws_li = []
    for sw in src:
        for cw in cmp:
            if sw == cw:
                if sw != ' ':
                    ws_li.append(sw)
    print(str(ws_li))

if __name__ == '__main__':
    with open('./doc.txt', 'r', encoding='utf-8') as f:
        contents = f.readlines()
        desc = ''
        for sent in contents:
            sent = sent.replace('\n',' ')
            desc += sent

    f.close()

    phars = desc.split('.')
    #for phar in phars:

    #tokenized(desc)

    kkma = Kkma()
    article = kkma.sentences(desc)
    print(article)

    twitter = Twitter()
    for sentence in article:
        out_str = twitter.nouns(sentence)
        print(out_str)


    words = komoran.pos(desc, join=True)
    #print(words)

    #print(phar)


    #str_cmp('집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.','집합(set)은 파이썬 2.3부터 지원하기 시작한 자료형으로')
    #main()


