
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos


# -------------------------------------------------------------------------------------
# name       : draw_mpl_base()
# description: Via matplotlib to draw base picture.
#
#              plot(xs, ys, zs, color, linestyle, linewidth, marker, 
#                   markeredgecolor, markeredgewidth, markerfacecolor, markersize, label)
#
# date       : 20210713
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def draw_mpl_base():
    x = np.arange(-np.pi, np.pi, 0.1)
    y1 = sin(x)
    y2 = cos(x)

    # 設定視窗的標題
    plt.figure("garyhsieh.twn")
    # 清除當前圖形內的所有內容
    plt.clf()

    # 放入x, y軸的資料內容, 圖例的名稱,
    plt.plot(x, y1, label = "sin func")
    #plt.plot(x, y2, color = "blue", label = "cos func")
    #plt.plot(x, y2, color = "green", label = "cos func")
    #plt.plot(x, y2, color = "red", label = "cos func")
    #plt.plot(x, y2, color = "cyan", label = "cos func")
    #plt.plot(x, y2, color = "magenta", label = "cos func")
    #plt.plot(x, y2, color = "yellow", label = "cos func")
    #plt.plot(x, y2, color = "black", label = "cos func")
    #plt.plot(x, y2, color = "white", label = "cos func")
    
    # ---- selected color ----
    # deep red
    #plt.plot(x, y2, color = "#9A0200", label = "cos func")
    # fire engine red
    #plt.plot(x, y2, color = "#FE0002", label = "cos func")
    # snot green
    #plt.plot(x, y2, color = "#9DC100", label = "cos func")
    # tealish
    #plt.plot(x, y2, color = "#24BCA8", label = "cos func")
    # mango
    #plt.plot(x, y2, color = "#FFA62B", label = "cos func")
    # oerulean, like blue.
    #plt.plot(x, y2, color = "#0485D1", label = "cos func")
    # lightish purple
    #plt.plot(x, y2, color = "#A552E6", label = "cos func")
    # plum purple
    #plt.plot(x, y2, color = "#4E0550", label = "cos func")

    # ---- linestyle ----
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-',label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '--',label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-.',label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = ':',label = "cos func")
    # ---- markrer ----
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = '.', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = 'o', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = '<', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = 's', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = '*', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = '|', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = 'h', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = 'd', label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = 'D', label = "cos func")
    # ---- markeredgewidth ----
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', marker = '.', markeredgewidth = 0.5, label = "cos func")
    # ---- lienwidth and markersize
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', linewidth = 1.5, marker = '.', markeredgewidth = 0.5, markersize = 6,label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', linewidth = 1, marker = '.', markeredgewidth = 0.5, markersize = 6,label = "cos func")
    #plt.plot(x, y2, color = "#4E0550", linestyle = '-', linewidth = 1, marker = 'o', markeredgewidth = 6, markersize = 0.5, label = "cos func")
    plt.plot(x, y2, color = "#4E0550", linestyle = '', linewidth = 1, marker = '.', markeredgewidth = 0, markersize = 6, label = "cos func")

    # 設定x, y軸的名稱
    plt.xlabel("x axis")
    plt.ylabel("y axis")

    # 設定圖例的顯示位置
    #plt.legend()
    plt.legend(loc = "best")
    #plt.legend(loc = "right")
    #plt.legend(loc = "center")
    #plt.legend(loc = "lower left")
    #plt.legend(loc = "upper right")
    #plt.legend(loc = "center left")

    # 顯示圖片
    plt.show()


if __name__ == "__main__":
    draw_mpl_base()
