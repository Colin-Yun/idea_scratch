# https://lovit.github.io/archives/#/page2

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
    for phar in phars:
        print(phar)

    #tokenized(desc)
    #str_cmp('집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.','집합(set)은 파이썬 2.3부터 지원하기 시작한 자료형으로')
    #main()


