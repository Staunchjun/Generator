import math

import cv2
import numpy as np
import sympy

from resolution import Resolution
from common import mm_to_resolution, singleton, DecimalRoundingRule, cal_ratio_and_mod
from window import Window
from init_conf import init_window, init_resolution


@singleton
class Graph:
    """
        生成图
        x,y默认为mm
    """

    @init_window
    @init_resolution
    def __init__(self, window_x_num: int, window_y_num: int, window_space_mm: float, window: Window = None,
                 resolution: Resolution = None):
        self._window_x_num = window_x_num
        self._window_y_num = window_y_num
        self._window_space = window_space_mm
        self._window = window
        self._resolution = resolution
        self._size_x: float = (self._window_x_num - 1) * self._window_space + self._window.x
        self._size_y: float = (self._window_y_num - 1) * self._window_space + self._window.y

    def window_distribute_x(self) -> [int, int]:
        window_space_x_resolution_floor = mm_to_resolution(self._window_space, self._resolution.x,
                                                           DecimalRoundingRule.FLOOR)
        window_space_x_resolution_ceil = mm_to_resolution(self._window_space, self._resolution.x,
                                                          DecimalRoundingRule.CEIL)
        x_floor_num, x_ceil_num = self.window_distribute_formula(window_space_x_resolution_floor,
                                                                 window_space_x_resolution_ceil,
                                                                 self._window_x_num, self.get_x_resolution(),
                                                                 self._window.get_x_resolution())
        print("window_distribute x ret:")
        print("x_floor_num:", x_floor_num)
        print("window_space_x_resolution_floor:", window_space_x_resolution_floor)
        print("x_ceil_num:", x_ceil_num)
        print("window_space_x_resolution_ceil:", window_space_x_resolution_ceil)
        return x_floor_num, window_space_x_resolution_floor, x_ceil_num, window_space_x_resolution_ceil

    def window_distribute_y(self) -> [int, int]:
        window_space_y_resolution_floor = mm_to_resolution(self._window_space, self._resolution.y,
                                                           DecimalRoundingRule.FLOOR)
        window_space_y_resolution_ceil = mm_to_resolution(self._window_space, self._resolution.y,
                                                          DecimalRoundingRule.CEIL)
        y_floor_num, y_ceil_num = self.window_distribute_formula(window_space_y_resolution_floor,
                                                                 window_space_y_resolution_ceil,
                                                                 self._window_y_num, self.get_y_resolution(),
                                                                 self._window.get_y_resolution())

        print("window_distribute y ret:")
        print("y_floor_num:", y_floor_num)
        print("window_space_y_resolution_floor:", window_space_y_resolution_floor)
        print("y_ceil_num:", y_ceil_num)
        print("window_space_y_resolution_ceil:", window_space_y_resolution_ceil)
        return y_floor_num, window_space_y_resolution_floor, y_ceil_num, window_space_y_resolution_ceil

    def window_distribute_formula(self, floor_var: int, ceil_var: int, sum_num: int, max_resolution: int,
                                  window_size: int) -> [int, int]:
        """
        计算公式：
            （108-1）*1.5625+0.72=167.9075mm，167.9075/25.4*1451.43=9594.7=9595
                1.5625/25.4*1451.43=89.3
                89*107+41=9564，90*107+41=9671
                89a+90b=9595-41
                a+b = 107
        :param floor_var:
        :param ceil_var:
        :param sum_num:
        :param max_resolution:
        :param window_size:
        :return:
        """
        print("****************window_distribute_formula****************")
        print("window_distribute_formula receiving... ")
        print("floor_var", floor_var)
        print("ceil_var", ceil_var)
        print("sum_num", sum_num)
        print("max_resolution", max_resolution)
        print("window_size", window_size)

        floor_num, ceil_num = sympy.symbols("floor_num ceil_num")
        formula_1 = floor_num + ceil_num - sum_num + 1
        formula_2 = floor_var * floor_num + ceil_var * ceil_num - max_resolution + window_size
        ret = sympy.solve([formula_1, formula_2], [floor_num, ceil_num])
        print("window_distribute_formula calculating... ")
        print(sympy.expand(formula_1))
        print(sympy.expand(formula_2))
        print("ret:", ret)
        return ret.get(floor_num), ret.get(ceil_num)

    @property
    def x(self) -> float:
        return self._size_x

    @property
    def y(self) -> float:
        return self._size_y

    def get_x_resolution(self) -> int:
        """
        获取x方向像素
        :return: x resolution
        """
        return mm_to_resolution(self._size_x, self._resolution.x, DecimalRoundingRule.ROUND)

    def get_y_resolution(self) -> int:
        """
        获取y方向像素
        :return: y resolution
        """
        return mm_to_resolution(self._size_y, self._resolution.y, DecimalRoundingRule.ROUND)

    def __str__(self):
        print("======Print graph var:======")
        print("size_x_mm: ", self._size_x)
        print("size_y_mm: ", self._size_y)
        print("x_resolution: ", self.get_x_resolution())
        print("y_resolution: ", self.get_y_resolution())
        self._window.__str__()

    def write_base_graph(self):
        image = np.zeros((self.get_x_resolution(), self.get_y_resolution(), 1), np.uint8)
        x_floor_num, x_floor_var, x_ceil_num, x_ceil_var = self.window_distribute_x()
        y_floor_num, y_floor_var, y_ceil_num, y_ceil_var = self.window_distribute_y()

        start_x = 0
        start_y = 0
        end_x = self._window.get_x_resolution()
        end_y = self._window.get_y_resolution()

        x_ratio, x_mod, x_flag = cal_ratio_and_mod(x_ceil_num, x_floor_num)
        y_ratio, y_mod, y_flag = cal_ratio_and_mod(y_ceil_num, y_floor_num)

        group_x: int = (x_floor_num + x_ceil_num - x_mod) / (x_ratio + 1)
        group_y: int = (y_floor_num + y_ceil_num - y_mod) / (y_ratio + 1)

        if y_flag == DecimalRoundingRule.FLOOR:
            for _ in range(group_y):
                for _ in range(y_ratio):
                    #  restore
                    start_y = 0
                    end_y = self._window.get_y_resolution()

                    self.draw_y_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var, x_mod,
                                    x_ratio)

                    # 如果floor比较多,先插入floor，再插入ceil.以ceil为基数
                    start_x = start_x + y_ceil_var
                    end_x = end_x + y_ceil_var
                # 补足最后一个 为 floor的，前面多加，这里要减去
                self.draw_y_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var, x_mod,
                                x_ratio)
                start_x = start_x + y_floor_var
                end_x = end_x + y_floor_var

            for _ in range(y_mod):
                self.draw_y_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var, x_mod,
                                x_ratio)
                start_x = start_x + y_floor_var
                end_x = end_x + y_floor_var

        if y_flag == DecimalRoundingRule.CEIL:
            for _ in range(group_y):
                for _ in range(y_ratio):
                    #  restore
                    start_y = 0
                    end_y = self._window.get_y_resolution()

                    self.draw_y_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var,
                                    x_mod,
                                    x_ratio)

                    # 如果ceil比较多,先插入ceil，再插入floor.以floor为基数
                    start_x = start_x + y_floor_var
                    end_x = end_x + y_floor_var
                # 补足最后一个 为 floor的，前面多加，这里要减去
                self.draw_y_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var, x_mod,
                                x_ratio)
                start_x = start_x + y_ceil_var
                end_x = end_x + y_ceil_var

            for _ in range(y_mod):
                self.draw_y_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var, x_mod,
                                x_ratio)
                start_x = start_x + y_ceil_var
                end_x = end_x + y_ceil_var
        cv2.imwrite("base_pic.bmp", image)

    def draw_y_dir(self, end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag, x_floor_var, x_mod,
                   x_ratio):
        # 如果ceil比较多,先插入ceil，再插入floor
        if x_flag == DecimalRoundingRule.CEIL:
            for _ in range(group_x):
                for _ in range(x_ratio):
                    cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                    start_y = start_y + x_floor_var
                    end_y = end_y + x_floor_var
                # 补足最后一个 为 floor的，前面多加，这里要减去
                cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                start_y = start_y + x_ceil_var
                end_y = end_y + x_ceil_var

            for _ in range(x_mod):
                cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                start_y = start_y + x_ceil_var
                end_y = end_y + x_ceil_var
        # 如果floor比较多,先插入floor，再插入ceil.以floor为基数
        if x_flag == DecimalRoundingRule.FLOOR:
            # 假设：10b 5a。
            # 按比例2：1
            # 插入：bba，bba
            for _ in range(group_x):
                for _ in range(x_ratio):
                    cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                    start_y = start_y + x_ceil_var
                    end_y = end_y + x_ceil_var
                # 补足最后一个 为 floor的，前面多加，这里要减去
                cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                start_y = start_y + x_floor_var
                end_y = end_y + x_floor_var

            for _ in range(x_mod):
                cv2.rectangle(image, (start_x, start_y - 1), (end_x, end_y - 1), (255, 255, 255), -1)
                start_y = start_y + x_floor_var
                end_y = end_y + x_floor_var