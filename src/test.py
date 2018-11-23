import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure

from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,NavigationToolbar2Kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color,Line,Rectangle

import numpy as np
import os
import matplotlib.pyplot as plt

print(os.environ['PATH'])

def press(event):
    print('press released from test', event.x, event.y, event.button)


def release(event):
    print('release released from test', event.x, event.y, event.button)


def keypress(event):
    print('key down', event.key)


def keyup(event):
    print('key up', event.key)


def motionnotify(event):
    print('mouse move to ', event.x, event.y)


def resize(event):
    print('resize from mpl ', event.width, event.height)


def scroll(event):
    print('scroll event from mpl ', event.x, event.y, event.step)


def figure_enter(event):
    print('figure enter mpl')


def figure_leave(event):
    print('figure leaving mpl')


def close(event):
    print('closing figure')





data="/media/sharath/Elements/RSF/seq78_single_shot_single_cable.txt"
shot=np.loadtxt(data)
#shot=np.array(shot)
print(shot.shape)

fig,ax=plt.subplots()
#fig.canvas.mpl_connect('button_press_event',press)
#fig.canvas.mpl_connect('button_release_event',release)
#fig.canvas.mpl_connect('figure_enter_event',figure_enter)
ax.imshow(shot,cmap='gray_r',aspect='auto')

canvas=fig.canvas


def callback(instance):
    canvas.draw()


class ShotView(App):
    title = 'Tagging Prototype'

    def build(self):
        fl=BoxLayout(orientation="vertical")
        a=Button(text="press",height=40,size_hint_y=None)
        a.bind(on_press=callback)
        fl.add_widget(canvas)
        fl.add_widget(a)
        return fl


if __name__=="__main__":
    ShotView().run()



#plt.show()
