import pyglet

ikkuna = pyglet.window.Window()

def hiiren_painaminen(leveys_sijainti, korkeus_sijainti, nappi, vaikutin):
    print('Painoit hiiren nappia', nappi, 'kohdassa', leveys_sijainti, korkeus_sijainti)

ikkuna.on_mouse_press = hiiren_painaminen

#VAIHTOEHTOINEN
#@ikkuna.event
#def on_mouse_press(leveys_sijainti, korkeus_sijainti, nappi, muutin):
#    print('Painoit hiiren nappia', nappi, 'kohdassa', leveys_sijainti, korkeus_sijainti)

pyglet.app.run()
