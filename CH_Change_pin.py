#!/usr/bin/env python
# -*- coding:utf-8 -*-
# #中文转化为拼音

"""
    Author:zf
    Time:2017-9-21
"""

__version__ = '0.9'
__all__ = ["PinYin"]

from xpinyin import Pinyin


def Change_ToPinYin(work):
    test = Pinyin()
    # print(work)
    string_q = test.get_pinyin(u"" + work, '')
    string_q = string_q.replace(' ', '_')
    # print(string_q)
    return string_q


# class PinYin(object):
#     def __init__(self, dict_file='word.data'):
#         self.word_dict = {}
#         self.dict_file = dict_file
#
#     def load_word(self):
#         if not os.path.exists(self.dict_file):
#             raise IOError("NotFoundFile")
#
#         with self.dict_file as f_obj:
#             for f_line in f_obj.readlines():
#                 try:
#                     line = f_line.split('    ')
#                     self.word_dict[line[0]] = line[1]
#                 except:
#                     line = f_line.split('   ')
#                     self.word_dict[line[0]] = line[1]
#
#     def hanzi2pinyin(self, string=""):
#         result = []
#         if not isinstance(string, str):
#             string = string.decode("utf-8")
#
#         for char in string:
#             key = '%X' % ord(char)
#             if not self.word_dict.get(key):
#                 result.append(char)
#             else:
#                 result.append(self.word_dict.get(key, char).split()[0][:-1].lower())
#
#         return result
#
#     def hanzi2pinyin_split(self, string="", split=""):
#         result = self.hanzi2pinyin(string=string)
#         if split == "":
#             return result
#         else:
#             return split.join(result)
#

if __name__ == "__main__":
    # test.load_word()
    string = "造船 船舶 公司"
    print(Change_ToPinYin(string))
    # print(string)
    # print(str(test.hanzi2pinyin(string=string)))
    # print(test.hanzi2pinyin_split(string=string, split="-"))
