import pyglet

ikkuna = pyglet.window.Window()

# Tässä esimerkissä luomme ohjelman, joka tulostaa käyttäjän näytölle "Kukkuu!"
# ja liikutaa sitä alaspäin ikkunassa,
# sekä tulostaa ikkunan alareunaan +-merkin, jos käyttäjä klikkaa tekstiä

kyltti = pyglet.text.Label('Kukkuu!') # Luodaan kyltti jossa lukee "Kukkuu!""
b = pyglet.text.Label('')

# Luodaan funktio, jossa määritellään, mitä tehdään jos käyttäjä klikkaa kylttiä

def hiiren_painaminen(leveys_sijainti, korkeus_sijainti, nappi, vaikutin):
    if kyltti.y - 10 < korkeus_sijainti < kyltti.y + 10:
        b.text = b.text + '+'

# Luodaan funktio, joka piirtää ikkunaan luodun kyltin

def piirrä():
    ikkuna.clear()
    kyltti.draw() 
    b.draw()

# Luodaan funktio, joka liikuttaa kylttiä ikkunassa

def a(kulunut_aika):
    kyltti.y -= 100 * kulunut_aika
    if kyltti.y < 0: 
        kyltti.y = 600 
        

pyglet.clock.schedule(a)

# Piirretään ikkunaan kyltti

ikkuna.on_draw = piirrä

ikkuna.on_mouse_press = hiiren_painaminen

pyglet.app.run()