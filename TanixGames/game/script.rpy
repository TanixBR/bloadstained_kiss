label splashscreen:
    
    scene black
    with Pause(1)
    show text "Tanix DEV Team Presents"
    with Pause(1)
    show text "Renpy Test 001 - Opening"
    with Pause(2)

    $ renpy.movie_cutscene("images/videos/mitama_opening.webm")

    return

label start:

    menu:
        "regular":
            pass
        "demo":
            jump demo
        "closet":        
            show screen dynamic_closet
            pause(10)
            

    "Olá Visitante"

    $cur_time = game_core.get_time()

    "Iniciamos nossa jornada [cur_time]"

    $cur_period = game_core.get_timeperiod()

    "O periodo atual é [cur_period]"    
    
    "Bem vindo ao Tanix Framework"
    
    "Iniciando com nosso ambiente mais simples"

    $ game_core.showhud()

    "Aqui temos nosso HUB basicão"

    show image game_core.chars["Yukito"]["regular"] at left
    game_core.chars["Yukito"]["char"] avatar "BOAAAAAA"

    show image game_core.chars["Shiruriru"]["regular"] at right
    game_core.chars["Shiruriru"]["char"] avatar "BOAAAAAA"

    show screen battle

    "Vamo Agora de Battle"

    return

label jankenpo:

    "Vamos Jogar Jankenpo!!!"

    "Agora vamos começar:"

    menu:
        "Jankenpo!"
        "Pedra":
            $ game_core.janken_choince = 0
        "Papel":
            $ game_core.janken_choince = 1
        "Tesoura":
            $ game_core.janken_choince = 2

    $ resultado = game_core.jankenpo()

    "Ora ora! [resultado]"

    "Vamos jogar denovo"

    jump jankenpo

    return

label demo:
    scene black
    game_core.chars["Yukito"]["char"] avatar "Que doideira essa coisa de Isekai"

    game_core.chars["Yukito"]["char"] avatar "Mas bom fazer o que né"

    game_core.chars["Shiruriru"]["char"] avatar "Yukito Yulito!!!!"

    game_core.chars["Yukito"]["char"] avatar "Que gritaria eh essa Shiruriru?"

    game_core.chars["Shiruriru"]["char"] avatar "Viu a Aruraru por ai, não acho ela em lugar algum!!!"

    game_core.chars["Mitama"]["char"] avatar "Aff pense em buscar ela!!!"

    game_core.chars["Yukito"]["char"] avatar "Ela deve ter se metido por aí"

    game_core.chars["Beltrun"]["char"] avatar "Yukito é uma emergencia Sequestraram a Aruraru"

    return