from microdot import Microdot, send_file, Response
import uasyncio as asyncio
from boot import leer_temperatura, controlar_buzzer, setpoint, buzzer_status, last_temp
import ujson

app = Microdot()
Response.default_content_type = 'application/json'

@app.route('/')
def index(req):
    return send_file('index.html')

@app.route('/styles/<path:path>')
def serve_css(req, path):
    return send_file('styles/' + path)

@app.route('/scripts/<path:path>')
def serve_js(req, path):
    return send_file('scripts/' + path)

@app.route('/setpoint', methods=['POST'])
def actualizar_setpoint(req):
    global setpoint
    data = req.json
    setpoint = data.get('setpoint', setpoint)
    return {'ok': True, 'nuevo_setpoint': setpoint}

@app.route('/estado')
def estado(req):
    global last_temp
    last_temp = leer_temperatura()
    controlar_buzzer(last_temp, setpoint)
    return {'temp': last_temp, 'buzzer': buzzer_status}

async def loop_sensor():
    while True:
        global last_temp
        last_temp = leer_temperatura()
        controlar_buzzer(last_temp, setpoint)
        await asyncio.sleep(2)

def start_server():
    app.run(debug=True, port=80)