define STREETWALKER = Character("STREETWALKER")
define RHODA = Character("RHODA")
define JUDITH = Character("JUDITH")

image Judith embarassed = "sprites/Judith_lacemaker_embarassed.png"

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
