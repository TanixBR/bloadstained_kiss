################################################################################
## General Functions
################################################################################

screen display_hover(img):
    add img 

screen dynamic_button(btn):
    vbox:
        xpos btn["xpos"]
        ypos btn["ypos"]  
        imagebutton:                          
                idle game_core.get_image(btn["idle"])
                if "hover" in btn:
                    hover game_core.get_image(btn["hover"])
                if "action" in btn:
                    if btn["action"][0] == "show":
                        action Show (btn["action"][1])
                    elif btn["action"][0] == "showmap":
                        action Function (game_core.showmap)
                    elif btn["action"][0] == "scene":
                        action Function (game_core.scene,btn["action"][1])
                    elif btn["action"][0] == "jump":
                        action Jump (btn["action"][1])
        if "title" in btn:
            text str(btn["title"])

screen movement(local):
    add game_core.get_image(game_core.scenes[local]["bg"])
    for btn in game_core.scenes[local]["imgbtn"]:
        use dynamic_button(btn)

################################################################################
## HUD of game
################################################################################

screen auto_hud(hud_items,local): 
    if local:
        use movement(local)    
    add "images/bg/bg_gui.png"
    #DYNAMIC ITEMS
    for i in game_core.dynamic_hud():
        use hud_display(i)     
    for i in hud_items:        
        use hud_display(i)

screen hud_display(hud_item):
    zorder 1        
    if type(hud_item) is dict:
        hbox:
            xalign hud_item["x"]                
            yalign hud_item["y"]                

            if "img" in hud_item:
                xpos hud_item["xpos"] 
                ypos hud_item["ypos"] 
                add game_core.get_image(hud_item["img"])
            if "title" in hud_item:
                text str(hud_item["title"]) xpos hud_item["tx"] ypos hud_item["ty"]
            if "imgbtn" in hud_item:
                for btn in hud_item["imgbtn"]:
                    use dynamic_button(btn)    

screen hud(hud_items): 
    zorder 0   
    for i in hud_items:        
        if type(i) is dict:
            hbox:
                xalign i["x"]                
                yalign i["y"]                

                add game_core.get_image(i["img"])
                if "title" in i:
                    text str(i["title"]) xpos i["tx"] ypos i["ty"]

################################################################################
## Game Maps
################################################################################

screen dynamic_map(map_data):
    modal True
    add game_core.get_image(map_data["bg"])

    if "imgbtn" in map_data:
        for btn in map_data["imgbtn"]:
            use dynamic_button(btn)

################################################################################
## Game Store
################################################################################

screen dynamic_store():
    modal True
    add game_core.get_image(game_core.store_bg)

    hbox:
        xpos 10
        ypos 10
        text "Your current ballance is $[game_core.money].00"

    hbox:
        xpos 200
        ypos 200
        grid 5 3:
            xalign 0.5
            yalign 0.5
            spacing 10
            for i in game_core.stores["kombini"]:
                frame:
                    xminimum 250
                    yminimum 250
                    vbox:
                        add game_core.get_image(i["img"])
                        text i["label"]
                        if i["status"]:
                            textbutton "Checkout" action Show("checkout")
                        else:
                            text "Purchased"
                    

screen checkout:
    modal True
    frame:
        xminimum 1000
        yminimum 1000
        vbox:
            text "Are you sure that you want to buy this item?"
            text "Please select the way that you want to receive the item:"
            textbutton "Get From Store - (need to go to a store)" action Hide("checkout")
            textbutton "Regular Mail - 10 days - Free" action Hide("checkout")
            textbutton "Express Mail - 5 days - $10" action Hide("checkout")
            textbutton "Comic Express Mail - 1 days - $50" action Hide("checkout")

################################################################################
## closet
################################################################################

screen dynamic_closet():
    modal True
    hbox:
        xpos 10
        ypos 10
        text "Tanix Closet System 001"
    hbox:
        xpos 200
        ypos 200
        grid 2 1:
            grid 5 3:
                xalign 0.5
                yalign 0.5
                spacing 10
                imagebutton idle game_core.get_image("icon-blackT.png") action Function(game_core.set_cloth, "icon-blackT.png")
                imagebutton idle game_core.get_image("icon-femaleTop.png") action Function(game_core.set_cloth, "icon-femaleTop.png")
                imagebutton idle game_core.get_image("icon-jeans.png") action Function(game_core.set_cloth, "icon-jeans.png")
                imagebutton idle game_core.get_image("icon-orangeT.png") action Function(game_core.set_cloth, "icon-orangeT.png") 
                imagebutton idle game_core.get_image("icon-pants01.png") action Function(game_core.set_cloth, "icon-pants01.png")
                imagebutton idle game_core.get_image("icon-pants02.png") action Function(game_core.set_cloth, "icon-pants02.png")
                imagebutton idle game_core.get_image("icon-whiteT.png") action Function(game_core.set_cloth, "icon-whiteT.png")
                imagebutton idle game_core.get_image("icon-yellowdress.png") action Function(game_core.set_cloth, "icon-yellowdress.png")             
            frame:
                xminimum 300
                yminimum 550
                vbox:
                    text "Cloth Selected"
                    add game_core.get_image(game_core.cloth)
    

################################################################################
## Battle Screen
################################################################################

screen battle():
    modal True
    frame:
        xpos 200
        ypos 500
        xminimum 500
        yminimum 250
        vbox:                
                text "Take your Action"                
                frame:                                            
                    xminimum 490
                    yminimum 200
                    hbox:
                        vbox:
                            text "HP 100"
                            text "MP 10"
                            text "ACT 5"
                        vbox:
                            xpos 100
                            textbutton "Physical Attack" action Hide("battle")
                            textbutton "Magical Attack" action Hide("battle")
                            textbutton "Item" action Hide("battle")
                            textbutton "Escape" action Hide("battle")

################################################################################
## Input Screen
################################################################################
screen input_name(default_value):

    #add "gui/input_name.png"

    text "ENTER YOUR NAME *THIS SHOULD BE REPLACED BY SOME GUI IMAGE"

    input default default_value:
        xalign 0.25
        yalign 0.43

################################################################################
## main_screen
################################################################################

screen main_screen:

    ### Screen settings

    default selected_menu = [0,None]

    modal True

    frame:
        pos (0,0)
        xysize (1920, 1080)

        margin (0,0)
        padding (0,0)

        background "#000000"

        frame:
            pos (375,5)
            xysize (1540, 50)
            background "#FFFFFF"

            hbox:
                text "Player: [game_player.player_name]":
                    xpos 10
                    color "#000000"

                text "Energy XXXX":
                    xpos 30
                    color "#000000"

                text "Money XXXX":
                    xpos 60
                    color "#000000"

                text "XP XXXXX":
                    xpos 90
                    color "#000000"

                text "BATTLE XXXX":
                    xpos 120
                    color "#000000"

        frame:
            pos (5, 5)
            xysize (365, 295)
            background "#FFFFFF"

            vbox:

                text "My CHAR":
                    color "#000000"


        frame:
            pos (5, 305)
            xysize (365, 720)
            background "#101000"

            vbox:

                text "Main Menu":
                    color "#000000"

                textbutton _("Character Select") action SetScreenVariable("selected_menu",[1,None])
                textbutton _("Mission Board") action SetScreenVariable("selected_menu",[2,None])
                textbutton _("Manager Character") action SetScreenVariable("selected_menu",[3,None])
                textbutton _("Manager Player") action SetScreenVariable("selected_menu",[4,None])
                textbutton _("SHOP") action SetScreenVariable("selected_menu",[5,None])

        ## Viewport with selected term's content.
        frame:
            pos (375, 65)
            xysize (520, 960)
            background "#101000"

            vbox:

                if selected_menu[0] == 0:
                    text "Please Select a Item in Main Menu":
                        color "#FFF"

                elif selected_menu[0] == 1:
                    text "Character Select":
                        color "#FFF"
                    vpgrid:
                        cols 3
                        rows 4

                        imagebutton:
                            idle "assets/characters/archer.png"
                            action SetScreenVariable("selected_menu",[1,"images/characters/ArcherGendai01_Normal.png","Character BIO\nName: Amy\nElement: Thunder"])

                        imagebutton:
                            idle "assets/characters/healer.png"
                            action SetScreenVariable("selected_menu",[1,"images/characters/HealerGendai02_Normal.png","Character BIO\nName: Judy\nElement: Wind"])

                        imagebutton:
                            idle "assets/characters/elf.png"
                            action SetScreenVariable("selected_menu",[1,"images/characters/ElfFantasy02_Normal.png","Character BIO\nName: Karin\nElement: Earth"])

                        text "Archer":
                            color "#FFF"

                        text "Healer":
                            color "#FFF"

                        text "Elf":
                            color "#FFF"

                        imagebutton:
                            idle "assets/characters/lancer.png"
                            action SetScreenVariable("selected_menu",[1,"images/characters/LancerFantasy01_Normal.png"])

                        imagebutton:
                            idle "assets/characters/thief.png"
                            action SetScreenVariable("selected_menu",[1,"images/characters/ThiefGendai01_Normal.png"])

                        imagebutton:
                            idle "assets/characters/warrior.png"
                            action SetScreenVariable("selected_menu",[1,"images/characters/KnightFantasy01_Normal.png"])

                        text "Lancer":
                            color "#FFF"

                        text "Thief":
                            color "#FFF"

                        text "Warrior":
                            color "#FFF"

                elif selected_menu[0] == 2:
                    text "Mission Board":
                        color "#FFF"

                    for i in gamePlayer.getMissions():
                        textbutton _(i) action SetScreenVariable("selected_menu", [2,i])

                elif selected_menu[0] == 3:
                    text "Manager Character":
                        color "#FFF"

                    textbutton _("Inventory") action SetScreenVariable("selected_menu",[3,0])
                    textbutton _("Equipment") action ShowMenu("Mission", action="avatar")
                    textbutton _("Skills") action ShowMenu("Mission", action="avatar")

                elif selected_menu[0] == 4:
                    text "Manager Player":
                        color "#FFF"

                    textbutton _("My Characters") action ShowMenu("Mission", action="avatar")
                    textbutton _("Level Up") action ShowMenu("Mission", action="avatar")
                    textbutton _("Inventory") action ShowMenu("Mission", action="avatar")
                    textbutton _("Money") action ShowMenu("Mission", action="avatar")

                elif selected_menu[0] == 5:
                    text "SHOP":
                        color "#FFF"

                    textbutton _("ITEMS") action SetScreenVariable("selected_menu",[5,0])
                    textbutton _("EQUIPMENT") action SetScreenVariable("selected_menu",[5,1])

        ## Viewport with selected term's content.
        frame:
            pos (900, 65)
            xysize (1015, 960)
            background "#101000"

            if selected_menu[0] == 0:
                    text "Please Select a Item in Main Menu":
                        color "#FFF"

            elif selected_menu[0] == 1:
                if selected_menu[1] == None:
                    text "Character Preview":
                        align (0.5, 0.5)
                        color "#FFF"
                elif selected_menu[1] != None:
                    background selected_menu[1]
                    if len(selected_menu) > 2:
                        text selected_menu[2]:
                            align (0.8, 0.1)
                            color "#FFF"

            elif selected_menu[0] == 2:
                if selected_menu[1] == None:
                    text "Enemy Preview":
                        align (0.5, 0.5)
                        color "#FFF"
                elif selected_menu[1] != None:
                    text selected_menu[1]:
                        align (0.2, 0.1)
                        color "#FFF"


            elif selected_menu[0]  == 3:
                if selected_menu[1] == None:
                    text "Manager Character Details":
                        align (0.5, 0.5)
                        color "#FFF"
                elif selected_menu[1] != None:
                    vbox:
                        for i in gamePlayer.getInventory():
                            textbutton _(i) action ShowMenu("Mission", action="avatar")

            elif selected_menu[0] == 4:
                text "Manager Player":
                    align (0.5, 0.5)
                    color "#FFF"

            elif selected_menu[0]  == 5:
                if selected_menu[1] == None:
                    text "SHOP Details":
                        align (0.5, 0.5)
                        color "#FFF"
                elif selected_menu[1] == 0:
                    vbox:
                        text "Item SHOP\n":
                            color "#FFF"
                        for i in gameShop.getItems():
                            textbutton _(i) action ShowMenu("Mission", action="avatar")
                elif selected_menu[1] == 1:
                    vbox:
                        text "Equipment SHOP\n":
                            color "#FFF"
                        for i in gameShop.getEquipment():
                            textbutton _(i) action ShowMenu("Mission", action="avatar")
                elif selected_menu[1] == 2:
                    vbox:
                        text "Power UPs SHOP\n":
                            color "#FFF"
                        for i in gameShop.getPowerUps():
                            textbutton _(i) action ShowMenu("Mission", action="avatar")

        ### Return button.
        imagebutton:

            pos (1750, 1040)

            idle "assets/mainscreen/return_idle.png"
            hover "assets/mainscreen/return_hover.png"

            action [ Hide("main_screen", dissolve), Return() ]



screen mission_selection(mission):

    add "images/misc/menubg.png"

    default mission_id = mission["mission_id"]

    hbox:

        imagebutton:
            xpos 380
            ypos 150
            idle "images/misc/arrow_back.png"
            action Hide("mission_selection"), ShowMenu("missions")
            hover "images/misc/arrow_back_hover.png"

        imagebutton:
            xpos 1420
            ypos 150
            idle "images/misc/close.png"
            hover "images/misc/close_hover.png"
            action Hide("mission_selection"), Hide("missions")

        text "MISSION":
            xpos 750
            ypos 150
            font "fonts/viner-hand-itc.ttf"
            size 48

    vbox:
        xpos 380
        ypos 250
        text "Mission ID: " + str(mission_id):
            size 25
            font "fonts/viner-hand-itc.ttf"
        text mission["description"]:
            size 36
            font "fonts/viner-hand-itc.ttf"
        text mission["details"]:
            xpos 10
            ypos 10
            size 28
            font "fonts/viner-hand-itc.ttf"

        vbox:
            ypos 50
            xpos 0
            vbox:
                text "Rank:":
                    style "menu_text2"
                hbox:
                    xpos 175
                    ypos -60
                    add "images/misc/rscreen/rstar.png"
                    add "images/misc/rscreen/rstar_empty.png"
                    add "images/misc/rscreen/rstar_empty.png"
                    add "images/misc/rscreen/rstar_empty.png"

        hbox:
            ypos 50
            xpos 0
            imagebutton:
                if game_player.selected_npc1 >= 0:
                    idle game_player.npc_list[game_player.selected_npc1]["side"]
                    hover game_player.npc_list[game_player.selected_npc1]["side_hover"]
                else:
                    idle "images/misc/misson_slot.png"
                    hover "images/misc/misson_slot_hover.png"
                action Show("select_player",select_party="game_player.selected_npc1")
            imagebutton:
                xpos 35
                if game_player.selected_npc2 >= 0:
                    idle game_player.npc_list[game_player.selected_npc2]["side"]
                    hover game_player.npc_list[game_player.selected_npc2]["side_hover"]
                else:
                    idle "images/misc/misson_slot.png"
                    hover "images/misc/misson_slot_hover.png"
                action Show("select_player",select_party="game_player.selected_npc2")

            textbutton "DEPART":
                xpos 400
                ypos 100
                text_style "menu_button2"
                action Hide("mission_selection"), Hide("missions"), Function(game_player.depart,mission), ShowMenu("mission_confirmation",mission)

screen mission_confirmation(mission):
    default status = game_player.quest_status
    if status == "Success":
        text "Mission Added" color '#eeeeee' 
    elif status == "Energy":
        text "Cannot Add Mission Due to Not enouth Energy" color '#eeeeee'

    textbutton "Confirm":
        xpos 400
        ypos 100
        text_style "menu_button2"
        action Return()

#screen mission_selection(mission):
#
#    add "images/misc/menubg.png"
#
#    hbox:
#
#        imagebutton:
#            xpos 380
#            ypos 150
#            idle "images/misc/arrow_back.png"
#            action Hide("mission_selection"), Show("missions")
#            hover "images/misc/arrow_back_hover.png"
#
#        imagebutton:
#            xpos 1420
#            ypos 150
#            idle "images/misc/close.png"
#            hover "images/misc/close_hover.png"
#            action Hide("missions")
#
#        text "MISSION":
#            xpos 750
#            ypos 150
#            font "fonts/viner-hand-itc.ttf"
#            size 48
#
#    vbox:
#        xpos 380
#        ypos 250
#        text mission["description"]:
#            size 36
#            font "fonts/viner-hand-itc.ttf"
#        text mission["details"]:
#            xpos 10
#            ypos 10
#            size 28
#            font "fonts/viner-hand-itc.ttf"
#        if mission["unique"] == '1':
#            text "UNIQUE MISSION":
#                xpos 10
#                ypos 10
#                size 28
#                font "fonts/viner-hand-itc.ttf"
#        textbutton "Start":
#            ypos 500
#            text_style "menu_button"
#            action Jump (["description"])

screen affection(select_party=None):

    default current_npc = 0

    add "images/misc/menubg.png"

    hbox:

        if select_party:
            imagebutton:
                xpos 380
                ypos 150
                idle "images/misc/arrow_back.png"
                hover "images/misc/arrow_back_hover.png"
                action Hide("affection")

        imagebutton:
            xpos 1420
            ypos 150
            idle "images/misc/close.png"
            hover "images/misc/close_hover.png"
            action Hide("affection")

        text "STATUS":
            xpos 750
            ypos 150
            font "fonts/viner-hand-itc.ttf"
            size 48

    vbox:
        xpos 500
        ypos 250

        text game_player.npc_list[current_npc]["name"]:
            font "fonts/viner-hand-itc.ttf"
            size 36
            line_spacing 30


        vbox:
            vbox:
                text "Strenght:":
                    style "menu_text2"


            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["strength"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["strength"])+" /50":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -50
            vbox:
                text "Magic:":
                    style "menu_text2"

            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["strength"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["magic"])+" /50":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -100
            vbox:
                text "Energy:":
                    style "menu_text2"

            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["energy"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["energy"])+" /10":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -150
            vbox:
                text "Affection:":
                    style "menu_text2"

            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["affection"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["affection"])+" /50":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -200
            vbox:
                text "Rank:":
                    style "menu_text2"
                hbox:
                    xpos 175
                    ypos -60
                    for i in range(game_player.npc_list[current_npc]["rank"]):
                        add "images/misc/rscreen/rstar.png"
                    for i in range(4-game_player.npc_list[current_npc]["rank"]):
                        add "images/misc/rscreen/rstar_empty.png"

    hbox:
        xpos 1150
        ypos 120
        imagebutton:
            xpos 0
            ypos 350
            idle "images/misc/arrow_left.png"
            hover "images/misc/arrow_left_hover.png"
            action SetScreenVariable( "current_npc", game_player.get_prevnpc(current_npc))

        add game_player.npc_list[current_npc]["image"] at resize_display

        imagebutton:
            xpos 0
            ypos 350
            idle "images/misc/arrow_right.png"
            hover "images/misc/arrow_right_hover.png"
            action SetScreenVariable( "current_npc", game_player.get_nextnpc(current_npc))

screen select_player(select_party=None):

    default current_npc = 0

    add "images/misc/menubg.png"

    hbox:

        if select_party:
            imagebutton:
                xpos 380
                ypos 150
                idle "images/misc/ok.png"
                hover "images/misc/ok_hover.png"
                action SetVariable(select_party,current_npc), Hide("select_player")

        imagebutton:
            xpos 1420
            ypos 150
            idle "images/misc/close.png"
            hover "images/misc/close_hover.png"
            action Hide("select_player")

        text "MISSION":
            xpos 710
            ypos 150
            font "fonts/viner-hand-itc.ttf"
            size 48

    vbox:
        xpos 500
        ypos 250

        text game_player.npc_list[current_npc]["name"]:
            font "fonts/viner-hand-itc.ttf"
            size 36
            line_spacing 30


        vbox:
            vbox:
                text "Strenght:":
                    style "menu_text2"


            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["strength"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["strength"])+" /50":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -50
            vbox:
                text "Magic:":
                    style "menu_text2"

            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["strength"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["magic"])+" /50":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -100
            vbox:
                text "Energy:":
                    style "menu_text2"

            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["energy"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["energy"])+" /10":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -150
            vbox:
                text "Affection:":
                    style "menu_text2"

            vbox:
                $ ui.bar(100, game_player.npc_list[current_npc]["affection"], xmaximum = 350, ymaximum = 30, top_bar=Frame("images/misc/rscreen/bar_full.png"), bottom_bar=Frame("images/misc/rscreen/bar_empty.png"), xpos = 180, ypos = -45)
                text str(game_player.npc_list[current_npc]["affection"])+" /50":
                    size 30
                    color '#ffffff'
                    font "fonts/viner-hand-itc.ttf"
                    xpos 335
                    ypos -85

        vbox:
            ypos -200
            vbox:
                text "Rank:":
                    style "menu_text2"
                hbox:
                    xpos 175
                    ypos -60
                    for i in range(game_player.npc_list[current_npc]["rank"]):
                        add "images/misc/rscreen/rstar.png"
                    for i in range(4-game_player.npc_list[current_npc]["rank"]):
                        add "images/misc/rscreen/rstar_empty.png"

    hbox:
        xpos 1150
        ypos 120
        imagebutton:
            xpos 0
            ypos 350
            idle "images/misc/arrow_left.png"
            hover "images/misc/arrow_left_hover.png"
            action SetScreenVariable( "current_npc", game_player.get_prevnpc(current_npc))

        add game_player.npc_list[current_npc]["image"] at resize_display

        imagebutton:
            xpos 0
            ypos 350
            idle "images/misc/arrow_right.png"
            hover "images/misc/arrow_right_hover.png"
            action SetScreenVariable( "current_npc", game_player.get_nextnpc(current_npc))
