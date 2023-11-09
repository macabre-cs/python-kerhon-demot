import pyglet
import time

# Katso "alku.py" selitykseksi
ikkuna = pyglet.window.Window()

# Katso "teksti.py" selitykseksi
teksti = pyglet.text.Label('')

# Nyt luomme funktion, joka päivittää näytetyn ajan aina kun kutsumme sitä
def päivitä_aika(dt):
    aika_nyt = time.strftime("%H:%M:%S")
    teksti.text = aika_nyt

# Katso "teksti.py" selitykseksi
@ikkuna.event
def on_draw():
    ikkuna.clear()
    teksti.draw()

pyglet.clock.schedule_interval(päivitä_aika, 1.0)  # Päivitetään kellon aika ikkunassa 1 sekunnin välein

pyglet.app.run()

# Voit tutkia lisää aiheesta osoitteessa: https://pyglet.readthedocs.io/en/latest/programming_guide/time.html
