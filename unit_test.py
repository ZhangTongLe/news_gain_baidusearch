import unittest

import requests


class TestStringMethods(unittest.TestCase):
    def test1(self):
        data = {
            'comp': '江南造船厂',
            'wordKey': '造船 船舶 公司 造船厂',
            'pages': '2'
        }
        r = requests.post('http://localhost:5000/eTensor/crawl/BaiDuSearchNews', data=data)
        # print('--------')
        # print(r.text)
        # print(879999999)
        Unimpeded_str = r.text
        str_pass = ''
        Unimpeded_list = ["true"]
        for Unimpeded in Unimpeded_list:
            if Unimpeded_str == Unimpeded:
                print(r.text)
                str_pass = "success"
            else:
                str_pass = r.text
        self.assertEqual(str_pass, 'success')
        # self.assertEqual(r.text, 'true')

        # def test2(self):
        #     data = {
        #         'comp': '江南造船厂',
        #         'wordKey': '造船 船舶 公司 造船厂'
        #     }
        #     r = requests.post('http://localhost:5000/eTensor/util/insert_comp', data=data)
        #     # print('--------')
        #     # print(r.text)
        #     # print(879999999)
        #     self.assertEqual(r.text, '成功')


if __name__ == '__main__':
    unittest.main()
