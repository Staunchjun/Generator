import math
from enum import Enum
from typing import Union


class DecimalRoundingRule(Enum):
    """
    CEIL 向上取整,
    FLOOR 向下取整
    ROUND 四舍五入
    """
    CEIL = 0,
    FLOOR = 1,
    ROUND = 2,
    RAW = 3,


def mm_to_resolution(mm: float, resolution: float, opt: DecimalRoundingRule = DecimalRoundingRule.FLOOR) -> Union[
    int, float]:
    """
       参考计算公式： 0.72 / 25.4 * 1451.43 = 41.14(向下取整)
    :param opt:
    :param mm:
    :param resolution:
    :return:
    """
    in_unit_mm: float = 25.4
    ret: float = mm / in_unit_mm * resolution
    if opt == DecimalRoundingRule.CEIL:
        return math.ceil(ret)
    elif opt == DecimalRoundingRule.ROUND:
        return round(ret)
    elif opt == DecimalRoundingRule.RAW:
        return ret
    return math.floor(ret)


class PermutationInfo:
    """
    用来保存排列信息的结构体
    """
    rule: DecimalRoundingRule
    ratio_a: int
    mod_a: int
    ratio_b: int
    mod_b: int
    group_num: int


def cal_ratio_and_mod(ceil_num: int, floor_num: int) -> [PermutationInfo]:
    """
    计算排列信息，根据两数数量，计算均匀分配的比例
    :param ceil_num: 下限数值
    :param floor_num: 上限数值
    :return:存排列信息的结构体
    """
    # 设定计算的临时变量
    high_num: int
    low_num: int
    # 记录占多数的一方
    rule: DecimalRoundingRule
    if floor_num > ceil_num:
        high_num = floor_num
        low_num = ceil_num
        rule = DecimalRoundingRule.FLOOR
    else:
        high_num = ceil_num
        low_num = floor_num
        rule = DecimalRoundingRule.CEIL

    ratio = round(high_num / low_num, 1)
    # 计算小数点后一位
    after_point = ratio - int(ratio)
    after_point = int(10 * round(after_point, 1))
    # 四舍五入
    if 1 <= after_point <= 2:
        ratio = int(ratio)
        after_point = 0
    elif 3 <= after_point <= 4:
        ratio = int(ratio)
        after_point = 5
    elif 6 <= after_point <= 7:
        ratio = int(ratio)
        after_point = 5
    elif 8 <= after_point <= 9:
        ratio = int(ratio) + 1
        after_point = 0

    if after_point != 5 and after_point != 0:
        raise Exception("数值计算错误，致命异常，非0.5的倍数")

    # 计算a/b比例
    ratio_a: int = 0
    ratio_b: int = 0
    # 如果后面为 0 ，则表示为x：1
    if after_point == 0:
        ratio_a = ratio
        ratio_b = 1
    #  如果后面不为 0 ，为 5，则表示是 x.5:1=>x:2
    elif after_point == 5:
        ratio_a = ratio * 2
        ratio_b = 2

    # 开始计算按照比例分配余多少出来, 可以分多少组
    cnt_high: int = 0
    cnt_low: int = 0
    group: int = 0

    #   计算分组数目，计算余数
    while cnt_high <= high_num and cnt_low <= low_num:
        cnt_high = cnt_high + ratio_a
        cnt_low = cnt_low + ratio_b
        group += 1

    # 多加的减回去
    cnt_high = cnt_high - ratio_a
    cnt_low = cnt_low - ratio_b
    group -= 1

    group_info = PermutationInfo()
    group_info.group_num = int(group)
    group_info.mod_a = int(high_num - cnt_high)
    group_info.mod_b = int(low_num - cnt_low)
    group_info.ratio_a = int(ratio_a)
    group_info.ratio_b = int(ratio_b)
    group_info.rule = rule
    return group_info


def singleton(cls_object):
    """
    单例包装函数
    :param cls_object: 单例对象
    :return: 单例对象
    """
    def inner(*args, **kwargs):
        if not hasattr(cls_object, "ins"):
            ins_object = cls_object(*args, **kwargs)
            setattr(cls_object, "ins", ins_object)
        return getattr(cls_object, "ins")

    return inner
