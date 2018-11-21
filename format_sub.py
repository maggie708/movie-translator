# This program serves to reformat the input bilingual subtitle files
# In the output file, there are 2 sentences separated by tab character in one line.
# The first sentence is english and followed by its corresponding Chinese.

import jieba
# jieba is a Chinese word segmentation module available on Github.
# Chinese vocabulary does not separate by space, so the Chinese subtitle needs to be parsed into vocabulary
# before feeding to the seq2seq model.

def write_to(fname, data):
    fo = open(fname, 'w')
    fo.write(data)
    fo.close()

def format_sub(fname):
    fo = open(fname, 'r')
    lines = [line.strip() for line in fo if line.strip()] # remove whitespaces in the starting or ending of line
    print(fname + ' : ' + lines.__len__().__str__() + ' sentences.')
    result = ''
    count = 0;
    while (count < lines.__len__()-1):
        bi = lines[count].split('\t')
        result += bi[0] + '\t' + ' '.join(jieba.cut(bi[1].replace(' ', ''), cut_all=False)) +'\n'
        count += 1
    write_to('data/eng-chi.txt', result)
    print('Formatting Completed.')

format_sub('data/eng-chi-source.txt')
