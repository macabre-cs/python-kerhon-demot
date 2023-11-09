import pyglet

ikkuna = pyglet.window.Window()

vasen_kyltti = pyglet.text.Label('', x=0)
oikea_kyltti = pyglet.text.Label('', x=400)

def esillä_paljon(kulunut_aika):
    vasen_kyltti.text = str(kulunut_aika)

pyglet.clock.schedule(esillä_paljon)

def esillä_välillä(kulunut_aika):
    oikea_kyltti.text = str(kulunut_aika)

pyglet.clock.schedule_interval(esillä_välillä, 1)

def piirrä():
    ikkuna.clear()
    vasen_kyltti.draw()
    oikea_kyltti.draw()

ikkuna.on_draw = piirrä


pyglet.app.run()
