import network

ssid = 'Cooperadora Alumnos'
password = ' '

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('Conectado a WiFi:', wlan.ifconfig())

from microdot import Microdot

app = Microdot()

@app.route('/')
def index(request):
    return '''
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidor</title>
  </head>
  <body>
    <main>
      <header>
        <h1>
          <span style="font-size:2.5em; font-weight:bold; letter-spacing:2px;">Aca con mi server de MicroDot B)!</span>
        </h1>
      </header>
      <section>
        <p>
          <span style="font-size:1.3em; color:#2c3e50;">Este servidor ta funcionando bien.</span>
        </p>
      </section>
    </main>
  </body>
</html>
    ''', 200, {'Content-Type': 'text/html'}

app.run(port=80)