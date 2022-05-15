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


def cal_ratio_and_mod(ceil_num: int, floor_num: int) -> [int, int, DecimalRoundingRule]:
    # 记录占多数的一方
    rule: DecimalRoundingRule
    if floor_num > ceil_num:
        ratio = math.floor(floor_num / ceil_num)
        mod = floor_num % ceil_num
        rule = DecimalRoundingRule.FLOOR
    else:
        ratio = math.floor(ceil_num / floor_num)
        mod = ceil_num % floor_num
        rule = DecimalRoundingRule.CEIL
    return ratio, mod, rule


def singleton(cls_object):
    def inner(*args, **kwargs):
        if not hasattr(cls_object, "ins"):
            ins_object = cls_object(*args, **kwargs)
            setattr(cls_object, "ins", ins_object)
        return getattr(cls_object, "ins")

    return inner
