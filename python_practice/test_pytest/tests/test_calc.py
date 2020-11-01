# -*- coding:utf-8 -*-
# @Time    : 2020/11/1 11:29
# @Author  : Nicole
# @File    : test_calc.py
import pytest
from hogwarts_taining.python_practice.test_pytest.core.calc import Calc

class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    # 正常值乘法
    @pytest.mark.parametrize('a, b, c', [
        [2, 3, 6], [0, 2, 0], [2.1, 1.2, 2.52], [2.1, 3, 6.3],
        [0.1, 0.1, 0.01], [0.01, 0.01, 0.00], [-1, -2, 2], [-1, 3, -3],
        [-0.1, 0.2, -0.02], [99999, 99999, 9999800001]])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 异常值乘法
    @pytest.mark.parametrize('a, b', [
        ["A", "B"], ["A", 0.1]
    ])
    def test_mul_exception(self, a, b):
        with pytest.raises(TypeError):
            assert self.calc.mul(a, b)

    # 正常值除法
    @pytest.mark.parametrize("a,b,c", [
        [10, 5, 2], [8.8, 2, 4.4], [9, 2, 4.5],
        [10, 3, 3.33], [5.2, 3.2, 1.62], [0.6, 0.3, 2],
        [0.7, 0.6, 1.17], [-6, -3, 2], [8, -4, -2],
        [-9, -3, 3], [-2.1, 4, -0.53], [-7, -3, 2.33],
        [0, 5, 0]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值除法
    @pytest.mark.parametrize("a, b", [
        ["A", "B"],
        [2, 0],
        [-0.5, 0]
    ])
    def test_div_exception(self, a, b):
        with pytest.raises((TypeError, ZeroDivisionError)):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        assert self.calc.mul(2, 3) == 6
        assert self.calc.div(6, 2) == 3
