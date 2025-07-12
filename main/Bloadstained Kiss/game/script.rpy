define STREETWALKER = Character("STREETWALKER")
define RHODA = Character("RHODA")
define JUDITH = Character("JUDITH")

#Judith Sprites
image Judith concerned              = "Judith/Judith_lacemaker_concerned.png"
image Judith content                = "Judith/Judith_lacemaker_content.png"
image Judith content_blush          = "Judith/Judith_lacemaker_content_blush.png"
image Judith embarassed             = "Judith/Judith_lacemaker_embarassed.png"
image Judith happy                  = "Judith/Judith_lacemaker_happy.png"
image Judith happy_blush            = "Judith/Judith_lacemaker_happy_blush.png"
image Judith sad                    = "Judith/Judith_lacemaker_sad.png"
image Judith smile                  = "Judith/Judith_lacemaker_smile.png"
image Judith smile_blush            = "Judith/Judith_lacemaker_smile_blush.png"
image Judith super_happy            = "Judith/Judith_lacemaker_super_happy.png"
image Judith super_happy_blush      = "Judith/Judith_lacemaker_super_happy_blush.png"
image Judith surprised              = "Judith/Judith_lacemaker_surprised.png"
image Judith worried                = "Judith/Judith_lacemaker_worried.png"

#Rhoda Sprites
image Rhoda angry        = "Rhoda/Rhoda_VPK_angry.png"
image Rhoda concerned    = "Rhoda/Rhoda_VPK_concerned.png"
image Rhoda neutral      = "Rhoda/Rhoda_VPK_neutral.png"
image Rhoda smile        = "Rhoda/Rhoda_VPK_smile.png"
image Rhoda surprised    = "Rhoda/Rhoda_VPK_surprised.png"

#Streetwalker Sprites
image Streetwalker angry = "Streetwalker/Streetwalker_angry.png"
image Streetwalker injured = "Streetwalker/Streetwalker_injured.png"
image Streetwalker smirk = "Streetwalker/Streetwalker_smirk.png"

transform shake:
    ease .06 xoffset 24
    ease .06 xoffset -24
    ease .05 xoffset 20
    ease .05 xoffset -20
    ease .04 xoffset 16
    ease .04 xoffset -16
    ease .03 xoffset 12
    ease .03 xoffset -12
    ease .02 xoffset 8
    ease .02 xoffset -8
    ease .01 xoffset 4
    ease .01 xoffset -4
    ease .01 xoffset 0



label splashscreen:

    show text "BloadStained Kiss Team" with fade

    pause 3.0

    show text "Psybelle" with dissolve

    pause 2.0

    show text "MaLevi" with dissolve

    pause 2.0

    show text "Aniki" with dissolve

    pause 2.0

    show text "Tanix" with dissolve

    pause 2.0

    show text """This can be any text just some Introdution Before main Screen \n
    Anyway this can remove, images can be place to show\n
    Or even none can be presented before main screen!!!!"""

    pause 5.0

    return

label start:

    jump prologue

    return
