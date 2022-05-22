import math

import cv2
import numpy as np
import sympy

from common import mm_to_resolution, DecimalRoundingRule, cal_ratio_and_mod, PermutationInfo
from conf import inject_graph_conf, GraphConf
from resolution import Resolution, inject_resolution
from window import Window, inject_window


class Graph:
    """
        生成图
        x,y默认为mm
    """

    @inject_graph_conf
    @inject_window
    @inject_resolution
    def __init__(self, conf: GraphConf = None, window: Window = None, resolution: Resolution = None):
        self._window_x_num = conf.window_num_x
        self._window_y_num = conf.window_num_y
        self._window_space_x = conf.window_space_x
        self._window_space_y = conf.window_space_y
        self._window = window
        self._resolution = resolution
        self._size_x: float = (self._window_x_num - 1) * self._window_space_x + self._window.x
        self._size_y: float = (self._window_y_num - 1) * self._window_space_y + self._window.y

    def window_distribute_x(self) -> [int, int]:
        window_space_x_resolution_floor = mm_to_resolution(self._window_space_x, self._resolution.x,
                                                           DecimalRoundingRule.FLOOR)
        window_space_x_resolution_ceil = mm_to_resolution(self._window_space_x, self._resolution.x,
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
        window_space_y_resolution_floor = mm_to_resolution(self._window_space_y, self._resolution.y,
                                                           DecimalRoundingRule.FLOOR)
        window_space_y_resolution_ceil = mm_to_resolution(self._window_space_y, self._resolution.y,
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
        """
        生成基础图像
        :return: 图像
        """
        # np.zeros行列
        image = np.zeros((self.get_y_resolution(), self.get_x_resolution(), 1), np.uint8)
        x_floor_num, x_floor_var, x_ceil_num, x_ceil_var = self.window_distribute_x()
        y_floor_num, y_floor_var, y_ceil_num, y_ceil_var = self.window_distribute_y()

        group_info_x: PermutationInfo = cal_ratio_and_mod(x_ceil_num, x_floor_num)
        group_info_y: PermutationInfo = cal_ratio_and_mod(y_ceil_num, y_floor_num)

        # 设定计算的临时变量
        high_num_y, high_var_y, low_num_y, low_var_y = self.set_cal_num(group_info_y, y_ceil_num, y_floor_num,
                                                                        y_ceil_var, y_floor_var)
        high_num_x, high_var_x, low_num_x, low_var_x = self.set_cal_num(group_info_x, x_ceil_num, x_floor_num,
                                                                        x_ceil_var, x_floor_var)

        # 如果ratio_b为2则表示 ratio a 需要 拆分了
        # 公式为 |x-y| = 1, x+y=ratio_a

        start_x = 0
        start_y = 0
        end_x = self._window.get_x_resolution()
        end_y = self._window.get_y_resolution()
        for _ in range(group_info_y.group_num):
            #  group 内循环
            #  等于2表示需要拆分a，不等于2则表示不需要拆分
            if group_info_y.ratio_b == 2:
                x_1 = int(math.ceil(group_info_y.ratio_a / 2))
                y_1 = int(group_info_y.ratio_a - x_1)
                for _ in range(x_1):
                    self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
                    start_y = start_y + high_var_y
                    end_y = end_y + high_var_y
                self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
                start_y = start_y + low_var_y
                end_y = end_y + low_var_y
                for _ in range(y_1):
                    self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
                    start_y = start_y + high_var_y
                    end_y = end_y + high_var_y
                self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
                start_y = start_y + low_var_y
                end_y = end_y + low_var_y
            else:
                for _ in range(group_info_y.ratio_a):
                    self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
                    start_y = start_y + high_var_y
                    end_y = end_y + high_var_y
                self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
                start_y = start_y + low_var_y
                end_y = end_y + low_var_y
        for _ in range(group_info_y.mod_a):
            self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
            start_y = start_y + high_var_y
            end_y = end_y + high_var_y
        for _ in range(group_info_y.mod_b):
            self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)
            start_y = start_y + low_var_y
            end_y = end_y + low_var_y

        # 补充最后多减去的一列
        self._draw_x(end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y)

        image = cv2.copyMakeBorder(image, 20 ,20, 20, 20, cv2.BORDER_CONSTANT)
        cv2.imwrite("base_pic.bmp", image)

    def _draw_x(self, end_y, group_info_x, group_info_y, high_var_x, image, low_var_x, start_y):
        #  restore
        start_x = 0
        end_x = self._window.get_x_resolution()
        #  group 内循环
        for _ in range(group_info_x.group_num):
            if group_info_x.ratio_b == 2:
                x = int(math.ceil(group_info_x.ratio_a / 2))
                y = int(group_info_x.ratio_a - x)
                for _ in range(x):
                    print((start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                    cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                    start_x = start_x + high_var_x
                    end_x = end_x + high_var_x
                cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                start_x = start_x + low_var_x
                end_x = end_x + low_var_x
                for _ in range(y):
                    cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                    start_x = start_x + high_var_x
                    end_x = end_x + high_var_x
                cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                start_x = start_x + low_var_x
                end_x = end_x + low_var_x
            else:
                for _ in range(group_info_x.ratio_a):
                    cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                    start_x = start_x + high_var_x
                    end_x = end_x + high_var_x
                cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
                start_x = start_x + low_var_x
                end_x = end_x + low_var_x
        # group 外补充mod
        for _ in range(group_info_x.mod_a):
            cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
            start_x = start_x + high_var_x
            end_x = end_x + high_var_x
        for _ in range(group_info_x.mod_b):
            cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)
            start_x = start_x + low_var_x
            end_x = end_x + low_var_x

        # 补充最后多减去的一列
        cv2.rectangle(image, (start_x, start_y), (end_x - 1, end_y - 1), (255, 255, 255), -1)

    def set_cal_num(self, group_info: PermutationInfo, ceil_num: int, floor_num: int, ceil_var: int,
                    floor_var: int) -> [int, int]:
        """
        根据规则分配最高值和最低值
        :param group_info:
        :param ceil_num:
        :param floor_num:
        :param ceil_var:
        :param floor_var:
        :return:
        """
        if group_info.rule == DecimalRoundingRule.FLOOR:
            high_num = floor_num
            high_var = floor_var
            low_num = ceil_num
            low_var = ceil_var
            return high_num, high_var, low_num, low_var
        if group_info.rule == DecimalRoundingRule.CEIL:
            high_num = ceil_num
            high_var = ceil_var
            low_num = floor_num
            low_var = floor_var
            return high_num, high_var, low_num, low_var
