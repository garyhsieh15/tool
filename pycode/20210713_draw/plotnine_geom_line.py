# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from plotnine import *
#from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib
#plt.rc('font',family='Times New Roman')
matplotlib.rcParams['font.family'] = 'Times New Roman'

df=pd.read_csv("MappingAnalysis_Data.csv")


# -------------------------------------------------------------------------------------
# name       : draw_theme_classic_BW()
# description: Via plotnine to draw gemo_line picture.
#
#              ggplot() + geon_line() + geon_point() + scale_fill_namual() + scale_shape_naumual() + 
#              theme_classic() + theme()
#                   
#
# date       : 20220710
# author     : garyhsieh_twn
# -------------------------------------------------------------------------------------
def draw_theme_classic_BW():
    pic =(ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) + 
            geom_line() +
            geom_point(size=4,colour="black") +
            scale_fill_manual(values=("#595959","#BFBFBF","black","white")) +
            scale_shape_manual(values=('o','s','D','^')) +
            theme_classic() +
            theme(text=element_text(size=12,colour = "black"),
                aspect_ratio =0.8,
                dpi=800,
                #figure_size=(4,4),
                figure_size=(5,5),
                legend_position=(0.32,0.75),
                legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
    
    pic.save("theme_classic_BW.png")
    pic += theme(text=element_text(size=12,colour = "black"),
            aspect_ratio =0.8,
            dpi=100,
            figure_size=(5,5),
            legend_position=(0.32,0.75),
            legend_background=element_rect(fill="none")) #shape=21,color="black",fill="red",size=3,stroke=0.1

    print(pic)


# -------------------------------------------------------------------------------------
# name       : draw_theme_classic_color()
# description: Via plotnine to draw gemo_line picture.
#
#              ggplot() + geon_line() + geon_point() + scale_fill_namual() + scale_shape_naumual() + 
#              theme_classic() + theme()
#                   
#
# date       : 20220710
# author     : garyhsieh_twn
# -------------------------------------------------------------------------------------
def draw_theme_classic_color():
    pic = (ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) +
            geom_line() +
            geom_point(size=4,colour="black") +
            scale_fill_manual(values=("#FF9641","#FF5B4E","#B887C3","#38C25D")) +
            scale_shape_manual(values=('o','s','D','^')) +
            scale_x_continuous(name="Time(d)",breaks=np.arange(0,21,2),limits=(0,20)) +
            scale_y_continuous(breaks=np.arange(0,91,10),limits=(0,90),expand =(0, 1)) +
            theme_classic() +
            theme(text=element_text(size=12,colour = "black"),
                aspect_ratio =0.8,
                dpi=800,
                figure_size=(5,5),
                legend_position=(0.32,0.75),
                legend_background=element_blank())) #shape=21,color="black",fill="red",size=3,stroke=0.1

    #p6.save("plotnine15.pdf") 
    pic.save("basic_color.png") 
    pic += theme(text=element_text(size=12,colour = "black"),
            aspect_ratio =0.8,
            dpi=100,
            figure_size=(5,5),
            legend_position=(0.32,0.75),
            legend_background=element_blank()) #shape=21,color="black",fill="red",size=3,stroke=0.1

    print(pic)

if __name__ == "__main__":

    draw_theme_classic_BW()
    draw_theme_classic_color()
