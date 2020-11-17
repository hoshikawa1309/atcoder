# 点と直線の距離を返す関数
# init_x, init_y は点の座標、それ以外は直線上の座標
def distance_from_point_to_line(init_x, init_y, x1, y1, x2, y2):
    import numpy as np
    u = np.array([x1 - x2, y1 - y2])
    v = np.array([init_x - x2, init_y - y2])
    ret_val = abs(np.cross(u, v) / np.linalg.norm(u))
    return ret_val
