import os
import Python_Juhe_BaiduSearch
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, Python_Juhe_BaiduSearch.app.config['DATABASE'] = tempfile.mkstemp()
        Python_Juhe_BaiduSearch.app.config['TESTING'] = True
        self.app = Python_Juhe_BaiduSearch.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(Python_Juhe_BaiduSearch.app.config['DATABASE'])

    def Nan_Chuan(self):
        data = {
            'comp': '江南造船厂',
            'pages': '2',
            # 'File_Address': '',
            'wordKey': '造船 船舶 公司 造船厂'
            # 'collection': 'Company_Names_zaochuanchang_baike'
        }
        rv = self.app.post('/eTensor/crawl/BaiDuSearchNews', data=data)
        r = str(rv.data, encoding='utf-8')
        # self.assertEqual(r, 'end...')
        print(str(r))
        Unimpeded_str = str(r)
        str_pass = ''
        Unimpeded_list = ['true', 'success', 'Program Is Ready !']
        for Unimpeded in Unimpeded_list:
            if Unimpeded in Unimpeded_str:
                str_pass = "success"
                break
            else:
                str_pass = str(r)
        # self.assertEqual(str_pass, 'success')
        assert 'success' in str_pass
        # self.assertEqual(str_pass, 'success')
        # assert 'success' in str_pass


if __name__ == '__main__':
    unittest.main()
