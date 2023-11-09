import pyglet

# Katso "alku.py" selitykseksi
ikkuna = pyglet.window.Window()

# Tässä esimerkissä tulostamme terminaaliin tekstin "Painoit nappia!" mikäli käyttäjä painaa jotain nappia.
def nappia_painetaan(nappi, vaikutin):
    print('Painoit nappia!')
    
ikkuna.on_key_press = nappia_painetaan

# VAIHTOEHTOISESTI
#@ikkuna.event
#def on_key_press(nappi, vaikutin):
#	print('Painoit nappia')


pyglet.app.run()
