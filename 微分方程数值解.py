# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:51:41 2023

@author: admin
"""

from scipy.integrate import odeint
import numpy as np

# 定义三阶微分方程组的函数
def equations(y, t):
    u, v, w = y  # y是包含三个未知函数的向量
    dydt = [v, w, -u]  # 这里假设三阶微分方程组为du/dt = v, dv/dt = w, dw/dt = -u
    return dydt

# 定义初始条件和时间间隔
y0 = [1.0, 0.0, 0.0]  # 初始条件
t = np.linspace(0, 10, 100)  # 时间间隔从0到10，将其均匀分成100个点

# 使用odeint函数求解微分方程组
sol = odeint(equations, y0, t)

# 打印数值解
print(sol)
