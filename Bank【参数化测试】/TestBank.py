from 工商 import bank_add, take_money, query_money
from 工商 import account_is, transfer
from unittest import TestCase
from write import get_data
from write import get_write
from ddt import ddt
from ddt import data
from ddt import unpack


@ddt
class TestBank(TestCase):

    @data(*get_data('bank.xlsx', '添加用户'))
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h, i, j):
        result = bank_add(a, b, c, d, e, f, g, h)
        get_write('bank.xlsx', '添加用户', 0, 9, '测试结果', 'bank.xlsx')
        if result == i:  # 让程序自动将测试结果写到excel表里。
            get_write('bank.xlsx', '添加用户', j, 9, '通过！', 'bank.xlsx')
        else:
            get_write('bank.xlsx', '添加用户', j, 9, '不通过！', 'bank.xlsx')

        # 断言
        self.assertEqual(i, result)


@ddt
class TestTake(TestCase):

    @data(*get_data('bank.xlsx', '存钱'))
    @unpack
    def testSave(self, a, c, d, e):
        result = account_is(a, 2, c)
        get_write('bank.xlsx', '存钱', 0, 3, '测试结果', 'bank.xlsx')
        if result == d:  # 让程序自动将测试结果写到excel表里。
            get_write('bank.xlsx', '存钱', e, 3, '通过！', 'bank.xlsx')
        else:
            get_write('bank.xlsx', '存钱', e, 3, '不通过！', 'bank.xlsx')

        # 断言
        self.assertEqual(d, result)


@ddt
class TestSave(TestCase):

    @data(*get_data('bank.xlsx', '取钱'))
    @unpack
    def testSave(self, a, b, c, d, e):
        result = take_money(a, b, c)
        get_write('bank.xlsx', '取钱', 0, 4, '测试结果', 'bank.xlsx')
        if result == d:  # 让程序自动将测试结果写到excel表里。
            get_write('bank.xlsx', '取钱', e, 4, '通过！', 'bank.xlsx')
        else:
            get_write('bank.xlsx', '取钱', e, 4, '不通过！', 'bank.xlsx')

        # 断言
        self.assertEqual(d, result)


@ddt
class TestTransfer(TestCase):

    @data(*get_data('bank.xlsx', '转账'))
    @unpack
    def testSave(self, a, b, c, d, e, f):
        result = transfer(a, b, c, d)
        get_write('bank.xlsx', '转账', 0, 5, '测试结果', 'bank.xlsx')
        if result == e:  # 让程序自动将测试结果写到excel表里。
            get_write('bank.xlsx', '转账', f, 5, '通过！', 'bank.xlsx')
        else:
            get_write('bank.xlsx', '转账', f, 5, '不通过！', 'bank.xlsx')

        # 断言
        self.assertEqual(e, result)


@ddt
class TestQuery(TestCase):

    @data(*get_data('bank.xlsx', '查询'))
    @unpack
    def testSave(self, a, c, d, e):
        result = query_money(a, c)
        get_write('bank.xlsx', '查询', 0, 3, '测试结果', 'bank.xlsx')
        if result == d:  # 让程序自动将测试结果写到excel表里。
            get_write('bank.xlsx', '查询', e, 3, '通过！', 'bank.xlsx')
        else:
            get_write('bank.xlsx', '查询', e, 3, '不通过！', 'bank.xlsx')

        # 断言
        self.assertEqual(d, result)
