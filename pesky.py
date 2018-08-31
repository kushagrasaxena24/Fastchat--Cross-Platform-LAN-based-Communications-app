from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
g = GridLayout(cols=2, spacing=5, size_hint_y=None)
b=BoxLayout(orientation='vertical')
t=TextInput(font_size=28,size_hint_y=None,height=60,text="Type Here",valign='Top')
def newLabel(instance):
	textIn=t.text
	if t.text is not "":
		lbl = Button(text=str(textIn), size_hint_y=None, height=len(textIn.splitlines())*30,halign='right',rgba=(0,0,0,0))
		lbl1 = Label(text=str(" "), size_hint_y=None, height=40,halign='left')
		g.add_widget(lbl1)
		g.add_widget(lbl) 
		t.text=""	



send=Button(text=str("Send"), size_hint_y=None, height=40,halign='right',valign='top')
send.bind(on_press=newLabel)
# Make sure the height is such that there is something to scroll.
g.bind(minimum_height=g.setter('height'))

s = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
s.add_widget(g)
b.add_widget(s)
b.add_widget(t)
b.add_widget(send)


runTouchApp(b)
