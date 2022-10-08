from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import datetime
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivymd.toast import toast
from kivy_design import KV

class MenuScreen(Screen):
    def range(self,d):
    	print(d)

class Screen2(Screen):
    txt = "\n[b][color=ff0099]  [*] istahfed 3la masroufek yee bro ;) [/color][/b]"

class Test(MDApp):
    t_date_range = []
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_string(KV)

    def on_save(self, instance, value, date_range):
        self.t_date_range = date_range
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
 # print instance, value,
        try :
            date_ch = "from "+str(date_range[0])+" \nto "+str(date_range[-1])
            self.root.get_screen('mainmenu').ids.date_range.text = date_ch
        except:
            pass

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    def next_screen(self):
        print("go to next screen ")
    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")

        #date_dialog.open()
       # date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    def num(self,ch):
        while len(ch)>0 and "0"<=ch[0]<="9" :
            ch = ch[1:]
        return not (len(ch)==0) 
    def procces(self):
        
        try:
            print(len(self.t_date_range))
            toast("worked!")
            starter = str(self.t_date_range[0])
            ender = str(self.t_date_range[-1])
            t = []
            year, month, day = int(str(starter)[:4]), int(str(starter)[5:7]), int(str(starter)[8:])+1
            last_day = int(str(ender)[8:])
            all_mony = int(self.root.get_screen('mainmenu').ids.all_mony.text)
            avg = int(self.root.get_screen('mainmenu').ids.avg.text)
            print(year,month,day,last_day,all_mony,avg)
            if day<=last_day and all_mony>=avg :
                all_mony-=avg
                t.append(f"Nhar[color=3333ff] {day-1} [/color]bch t3adih o yab9alek[color=3333ff] {all_mony*0.001} TND [/color].  ")

                all_mony-=avg
            while day<=last_day and all_mony>=avg :
                t.append(f"Nhar[color=3333ff] {day} [/color]bch t3adih o yab9alek[color=3333ff] {all_mony*0.001} TND [/color].  ")
                day+=1
                all_mony-=avg
                
                print(day,all_mony)
            if all_mony > 0 :
                    t.append(f"Youm[color=3333ff] {day} [/color]lezmek t3adyh b {all_mony} . ")
            if last_day>day :
                for i in range(day+1,last_day+1):
                    t.append(f"Nhar[color=3333ff] {i} [/color]ma3ndek fih [color=ff3333]hata frank[/color] !")
            t.append("\n \n")
            for i in t :
                self.root.ids.scr_2.ids.label.text += '\n' + str(i)
            #   self.root.ids.scr_2.ids.label.text += all_mony + "\n" + str(last_day)
                self.root.ids.scr_2.ids.scroll_view.scroll_y = 0
        except:
            toast("Failed")
            if self.num(self.root.get_screen('mainmenu').ids.all_mony.text) :
                toast("qadeh 3andek flous entier!")
            if self.num(self.root.get_screen('mainmenu').ids.avg.text) :
                toast("qadeh tosref flous entier!")
            if len(self.t_date_range)<=1 :
                toast("qadeh 3andek flous entier!")

Test().run()
