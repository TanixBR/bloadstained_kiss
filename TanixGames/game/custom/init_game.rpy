init +1 python:

    import json
    import os.path
    import base64
    import os
    import logging
    import logging.handlers    
    from datetime import datetime,timedelta
    from random import randint

     

    class base_class(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()
        
        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    class core(base_class):
        """Game Core Class
        """

        def __init__(self):
            """Game Code Initilalization
            """

            self.cloth = None

            self.tanix_log = self.start_log()
            self.tanix_log.info(f"Starting Game")
            self.content = None
            self.datafile = "game.data"
            self.images = {}
            self.load_images()

            self.store_bg = "bg_konbini.png"

            self.hud_items = [{"x":0, "y":0, "imgbtn":[
            {"xpos":1800,"ypos":30,"idle":"status_idle.png","hover":"status_hover.png","action":["showmap"]},
            {"xpos":1600,"ypos":30,"idle":"map_idle.png","hover":"map_hover.png","action":["showmap"]},
            {"xpos":1400,"ypos":30,"idle":"glove_idle.png","hover":"glove_hover.png","action":["jump","jankenpo"]},
            {"xpos":1200,"ypos":30,"idle":"inventory_idle.png","hover":"inventory_hover.png","action":["show","city_map"]},
            {"xpos":1000,"ypos":30,"idle":"shop_idle.png","hover":"shop_hover.png","action":["show","dynamic_store"]},
            {"xpos":800,"ypos":30,"idle":"agenda.png","action":["show","dynamic_store"]},
            {"xpos":600,"ypos":30,"idle":"message.png","action":["show","dynamic_store"]},
            {"xpos":400,"ypos":30,"idle":"phone.png","action":["show","dynamic_store"]}]}]

            self.maps = {"map":{"bg":"bigcity_map.png",
                "imgbtn":[{"xpos":300,"ypos":300,"idle":"green_pin.png","title":"Work","action":["scene","bg_konbini.png"]},
                {"xpos":600,"ypos":100,"idle":"yellow_pin.png","title":"University","action":["scene","bg_school.png"]},
                {"xpos":900,"ypos":700,"idle":"green_pin.png","title":"Park","action":["scene","bg_park.png"]},
                {"xpos":400,"ypos":800,"idle":"black_pin.png","title":"Home","action":["scene","home"]},
                {"xpos":700,"ypos":300,"idle":"blue_pin.png","title":"Night Club","action":["scene","bg_park.png"]},
                {"xpos":1000,"ypos":300,"idle":"red pin.png","title":"????????","action":["scene","bg_park.png"]}]}            
                }

            self.scenes = {"home":{"bg":"bg_livingroom_day.png",
            "imgbtn":[{"xpos":300,"ypos":300,"idle":"green_pin.png","title":"Kitchen","action":["scene","kitchen"]},
            {"xpos":900,"ypos":300,"idle":"green_pin.png","title":"Bedroom","action":["scene","bedroom"]}]},
            "kitchen":{"bg":"bg_kitchen_day.png",
            "imgbtn":[{"xpos":300,"ypos":300,"idle":"green_pin.png","title":"Liveroom","action":["scene","home"]}]},
            "bedroom":{"bg":"bg_bedroom_day.png",
            "imgbtn":[{"xpos":300,"ypos":300,"idle":"green_pin.png","title":"Liveroom","action":["scene","home"]}]}     
                }

            self.stores = {"kombini":[{"img":"cookie-01-icon.png", "label":"Cookies", "status":True},
            {"img":"sandwish-icon.png", "label":"Sandwish", "status":True},
            {"img":"dress-icon.png", "label":"Dress", "status":True},
            {"img":"necless01-icon.png", "label":"Ac01", "status":True},
            {"img":"necless02-icon.png", "label":"Ac02", "status":True},
            {"img":"chess-icon.png", "label":"Chess", "status":True},
            {"img":"clock-icon.png", "label":"Ckock", "status":True},
            {"img":"computer-icon.png", "label":"Computer", "status":True},
            {"img":"flower-icon.png", "label":"flower", "status":True},
            {"img":"gift-icon.png", "label":"gift", "status":True},
            {"img":"kiss-01-icon.png", "label":"kiss", "status":True},
            {"img":"heart-icon.png", "label":"heart", "status":True}
            ]}

            self.chars = {"Aruraru":{"avatar":"Aruraru_Photo.png"},
            "Atar":{"avatar":"Atar_Photo.png"},
            "Beltrun":{"avatar":"Beltrun_Photo.png"},
            "Dakini":{"avatar":"Dakini_Photo.png"},
            "Gaia":{"avatar":"Gaia_Photo.png"},
            "Loki":{"avatar":"Loki_Photo.png"},
            "Mitama":{"avatar":"Mitama_Photo.png"},
            "Rishu":{"avatar":"Rishu_Photo.png"},
            "Shiruriru":{"avatar":"Shiruriru_Photo.png"},            
            "Yukito":{"avatar":"Yukito_Photo.png"}}

            self.init_chars()
            
            self.janken_choince = 0
            self.current_time = datetime(2023, 1, 1, 8, 00)
            self.ref_energytime = datetime.now()
            self.energy = 10
            self.money = 7359

        def start_log(self):            
            l = logging.getLogger("tanix_log")
            formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
            fileHandler = logging.FileHandler(f"{config.gamedir}/tanix.log", mode='w')
            fileHandler.setFormatter(formatter)
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)

            l.setLevel(logging.DEBUG)
            l.addHandler(fileHandler)
            l.addHandler(streamHandler)   
                        
            return logging.getLogger("tanix_log")        
            
        def load_images(self):
            for path in renpy.list_files():
                if path.startswith("images/"):
                    path_list = path.split("/")
                    self.images[path_list[-1]] = path

        def get_image(self,img):            
            if img in self.images:
                output = self.images[img]                
            else:
                output = None
            return output

        def init_chars(self):
            for key, value in self.chars.items():
                char_color = "#c8ffc8"
                self.tanix_log.info(f"Char {value}")
                self.chars[key]["char"] = Character(key, who_color=char_color, image=key)
                if "avatar" in value:
                    renpy.image(f"side {key} avatar",self.get_image(value["avatar"]))
                if self.get_image(f"{key}.png"):
                    self.chars[key]["regular"] = self.get_image(f"{key}.png")

        def dynamic_hud(self):
            items = [{"x":0, "y":0, "xpos":30, "ypos":10, "img":f"icon_{self.get_timeperiod()}.png"}, 
            {"x":0, "y":0, "xpos":0, "ypos":0, "title":f"{self.current_time.strftime('%A')}","tx":20,"ty":120},
            {"x":0, "y":0, "xpos":0, "ypos":0, "title":f"{self.current_time.strftime('%B %d')}","tx":20,"ty":160}]
            return items

        def showhud(self):                     
            renpy.show_screen("auto_hud",hud_items=self.hud_items,local=None)

        def showmap(self):
            renpy.show_screen("dynamic_map",map_data=self.maps["map"])

        def scene(self,location):                  
            renpy.hide_screen("dynamic_map")
            renpy.show_screen("auto_hud",hud_items=self.hud_items,local=location)

        def set_cloth(self, cloth):
            self.cloth = cloth

        def jankenpo(self):
            computer_choice = randint(0,2)
            if self.janken_choince == computer_choice:
                return "Empate"
            elif computer_choice == 0:
                if self.janken_choince == 1:
                    return "Jogador Ganhou, Papel ganhou da pedra"
                elif self.janken_choince == 2:
                    return "Jogador Perdeu, Tesoura perdeu para Pedra"
            elif computer_choice == 1:
                if self.janken_choince == 0:
                    return "Jogador Perdeu, Pedra perdeu para Papel"
                elif self.janken_choince == 2:
                    return "Jogador Ganhou, Tesoura ganhou do Papel"
            elif computer_choice == 2:
                if self.janken_choince == 0:
                    return "Jogador Ganhou, Pedra ganhou da Tesoura"
                elif self.janken_choince == 1:
                    return "Jogador Perdeu, Papel perdeu para Tesoura"

        def get_time(self):
            return self.current_time.strftime("%d/%m/%Y %H:%M:%S")
        
        def get_timeperiod(self):    
            if self.current_time.hour < 12:
                return "Morning"
            elif self.current_time.hour < 18:
                return "Afternoon"
            elif self.current_time.hour < 22:
                return"Evening"
            elif self.current_time.hour >= 22 and self.current_time.hour < 6:
                return "Night"

        def next_hour(self):
            self.current_time = self.current_time + timedelta(hours=1)

        def check_energy(self):
            check_date = datetime.now() + timedelta(hours=-1)            
            if check_date > self.ref_energytime:            
                self.ref_energytime = datetime.now()
                self.energy = 10
        
        def use_energy(self,unit):
            self.tanix_log.info(f"Unit {unit}")
            if self.energy >= unit:
                self.energy -= unit
                self.tanix_log.info(f"energy {self.energy}")
                return self.energy
            else:
                false

        def enc_data(self,inputData):
            return base64.b64encode(inputData)
        
        def dec_data(self,inputData):
            return base64.b64decode(inputData)

        def load_data(self):
            with open("{}/{}".format(config.gamedir,self.datafile), 'rb') as f:
                fileData = f.read()
            self.content = json.loads(self.dec_data(fileData).decode("utf-8"))
        
        def save_data(self):
            with open(self.save_name, 'wb') as f:
                f.write(self.enc_data(self.content))   

################################################################################
## System Vars
################################################################################

    config.developer = True

################################################################################
## Game Objects
################################################################################

    game_player = player()
    game_core = core()  
    
################################################################################
## CG
################################################################################

################################################################################
## MUSIC BOX
################################################################################


################################################################################
## CHARACTERS
################################################################################

    MC = Character("Player Name", color='#f00055')

################################################################################
## IMAGES AND VIDEOS
################################################################################


################################################################################
## SPRITES
################################################################################
