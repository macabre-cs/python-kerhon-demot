import pyglet

ikkuna = pyglet.window.Window()

muodot = []

# Tässä esimerkissä luomme simppelin ohjelman joka piirtää ikkunaan eri värisen pallon käyttäjän klikkaamaan kohtaan.

def hiiren_painaminen(leveys_sijainti, korkeus_sijainti, nappi, vaikutin):
    muodot.append(pyglet.shapes.Circle(leveys_sijainti, korkeus_sijainti, 30,
                                       color=(leveys_sijainti, korkeus_sijainti,0)))
    
ikkuna.on_mouse_press = hiiren_painaminen

def piirrä():
    for muoto in muodot:
        muoto.draw()

ikkuna.on_draw = piirrä

pyglet.app.run()