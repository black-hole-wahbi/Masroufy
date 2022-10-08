KV = '''
<MenuScreen>:
    name: 'mainmenu'
    MDFloatLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "MASROUFY !"
            elevation: 14
            pos_hint: {'top': 1}
        MDTextField:
            id: all_mony
            hint_text: "qadeh 3andek flous"
            helper_text: "how much u have ?"
            helper_text_mode: "on_focus"
            icon_right: "cash-multiple"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.75}
            size_hint_x:None
            width:root.width * 0.5
        MDTextField:
            id: avg
            hint_text: "qadeh tosref"
            helper_text: "what do u spend daily ?"
            helper_text_mode: "on_focus"
            icon_right: "cash"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.58}
            size_hint_x:None
            width:root.width * 0.5
        MDRectangleFlatButton:
            text: "Open date picker"
            pos_hint: {'center_x': .5, 'center_y': .4}
            on_release: app.show_date_picker()
        MDRoundFlatButton:
    		
 		   text: "Procces your information"
 		  # width: root.width * .6
#            icon: "language-python"
#            theme_icon_color: "Custom"
#            icon_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5, "center_y": .1}
            on_press: app.procces()
            on_release:
                if not app.num(all_mony.text): root.manager.current = 'screen2'

        MDLabel:
        	id : date_range
        	text: ""
        	halign : "center"
        	pos_hint:{"center_x": .5 ,"center_y": .3}

<Screen2>:
    name: 'screen2'
    BoxLayout:
        size_hint_y: None
        height: root.width * .8
        pos_hint:{"top":1}
        spacing: 19
        orientation: "vertical"

        ScrollView:
            id: scroll_view
            always_overscroll: False
            BoxLayout:
                size_hint_y: None
                height: self.minimum_height
                #orientation: 'vertical'
                MDLabel:
                    id: label
                    markup : True
                    halign : "center"
                    text: root.txt
                    size_hint_y: None
                    size: self.texture_size 
        
                    
    MDRectangleFlatButton:
        text: "Back"
        pos_hint : {"center_x": .5,"center_y": .1}
        on_release:
            root.manager.current = 'mainmenu'
            root.manager.transition.direction = "right"
    
    
ScreenManager:
    MenuScreen:
        id: scr_1
        
    Screen2:
        id: scr_2


'''
