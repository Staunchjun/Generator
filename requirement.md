# tool
## requirement
    期望：
    输入：开窗x，y方向个数，单个开窗x,y方向像素点数目，分辨率，开窗间距，边缘填充像素行数（50）
    输出：图

### info
    开窗总数一样是108*96个（数据输入）
    分辨率1451.43*1441.12（1451.43当于像素点17.5um,1441.12相当于360.28*4pass）
### base
    开窗像素点全部取整41*23（去掉41.14*23.26的小数位）
    换算公式：0.72/25.4*1451.43=41.14(向下取整)
    开窗大小0.72*0.41mm，（41*23）
    开窗间距是1.5625mm，1.5625/25.4*1451.43=89.28，89，88.6 （左上角向下，左下角向右）
    画图由坐标系00开始，后续补充padding
    开窗总数一样是108*96个（数据输入）
    先生成开窗。
    （108-1）*1.5625+0.72=167.9075mm，167.9075/25.4*1451.43=9594.7=9595
    1.5625/25.4*1451.43=89.3
    89*107+41=9564，90*107+41=9671
    89a+90b=9595-41
    a+b = 107
    b 均匀插入a
    假设：10b 5a。
    按比例2：1插入，bba，bab(
    b21：a4
    bbabb,bbabb,bbabb,bbabb,b,

        # 如果floor比较多,先插入floor，再插入ceil.以ceil为基数
        if y_flag == DecimalRoundingRule.FLOOR:
            for _ in range(group_y):
                for _ in range(y_ratio):
                    #  restore
                    start_y = 0
                    end_y = self._window.get_x_resolution()

                    end_y, start_y = self.draw_x_dir(end_x, end_y, group_x, image, start_x, start_y, x_ceil_var, x_flag,
                                                     x_floor_var, x_mod, x_ratio)
                    # 如果floor比较多,先插入floor，再插入ceil.以ceil为基数
                    cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (255, 255, 255), -1)
                    start_x = start_x + y_ceil_var
                    end_x = end_x + y_ceil_var
                # 补足最后一个 为 floor的，前面多加，这里要减去
                cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (255, 255, 255), -1)
                start_x = start_x + y_floor_var
                end_x = end_x + y_floor_var

            for _ in range(y_mod):
                cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (255, 255, 255), -1)
                start_x = start_x + y_floor_var
                end_x = end_x + y_floor_var

