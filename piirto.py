import pyglet

# Katso "alku.py" selitykseksi
ikkuna = pyglet.window.Window()

# Luomme kuvan. Paikka, josta kuva löytyy kerrotaan ohjelmalle sulkeiden eli () sisällä.
kuva_hymiöstä = pyglet.resource.image('hymiö.png')

# Luomme kyltin. Se mitä kyltissä lukee on määritelty sulkeiden eli () sisälle.
kyltti = pyglet.text.Label('Kukkuu!')

# Mutta miten piirrämme kuvan ja kyltin näytölle? Esitämme kaksi tapaa, joiden lopputulos on sama.
# Toinen tavoista on kommentoitu pois.

# Molemmissa tavoissa meidän pitää määritellä mitä Pyglet tekee, kun haluaa piirtää näytölle.
# Tämän määrittelemme aliohjelmalla! Eli meillä on pieni ohjelma, joka toteutetaan, kun Pyglet
# Haluaa piirtää näytölle
def piirrä():
    # Ensin pyyhimmi ikkunnan aijemmat töhryt
    ikkuna.clear()

    # Piirrämme kuvan kohtaan 0, 0. Kannattaa tutustua materiaaliin koordinaateista.
    kuva_hymiöstä.blit(0, 0)

    # Piirrämme kyltin
    kyltti.draw()

# Nyt meillä on haluamamme aliohjelma, mutta pyglet ei vielä tiedä sen olemassa oloa.
# Kerromme pygletin ikkunalle, että se voi käyttää "piirrä" aliohjelmaa:
ikkuna.on_draw = piirrä

# VAIHTOEHTOINEN TAPA TOTEUTTAA PIIRTÄMINEN!:
#ikkuna.event
#def on_draw():
#    ikkuna.clear()
#    kuva_hymiöstä.blit(0, 0)
#    kyltti.draw()

# Katso "alku.py" selitykseksi
pyglet.app.run()

# Voit tutustua seuraavaksi siihen kuinka vaikuttaa kuvien kokoon näytöllä tai näppäinten tai hiiren paineluun.
