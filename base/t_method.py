# coding:utf-8
import unittest
from TestCase.demo import RunMain


class TestMethod(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):  #类方法定义
    #     print "类执行之前的方法"
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print "类执行之后的方法"

    #每次方法前执行
    def setUp(self):
        print 'test-->setup 每次方法前执行'
        self.run = RunMain()

    def test_03(self):
        print "test_03"

    def test_02(self):
        url = "http://web-api-test.energymost.com/api/vee/getscanswitch"
        data = {
            "hierarchyId": 353069
        }
        method = "get"
        run =RunMain()
        r =run.run_main(url,method,data)
        print "第二个case\n"
        print r.status_code

    def test_01(self):
        url = "http://web-api-test.energymost.com/api/vee/getdatastructure"
        data = {
            "UserId": 312135,
            "CustomerId": 347373
        }
        method = 'post'
        #run = RunMain(url=url,method="POST",data=data)
        res = self.run.run_main(url,method,data)
        print type(res)
        #self.assertEqual(r.status_code,200)
        print "test_01"
        r = res.status_code
        a = {}
        self.assertEqual(r,200,"验证是否返回200") #参数是否相等



    # 每次方法后执行
    def tearDown(self):
        print"test-->tearDown 每次方法后执行"


'''
断言
        self.assertEqual(a,b)
        self.assertNotEqual(a,b)
        self.assertTrue(x)
        self.assertFalse(x)
        self.assertIs(a,b)
        self.assertIsNot(a,b)
        self.assertIsNone(x)
        self.assertIsNotNone(x)
        self.assertIn(a,b)
        self.assertNotIn(a,b)
        self.assertIsInstance(a,b)
        self.assertNotIsInstance(a,b)
'''
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_02'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
   # unittest.main()


