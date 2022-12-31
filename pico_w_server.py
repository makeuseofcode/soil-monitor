from microdot import Microdot
import mm_wlan, pico_w_server
from pmon import PlantMonitor


ssid = '2.4 GHz SSID'
password = 'insert password'

html = """
<!DOCTYPE html>
<!-- <meta http-equiv="refresh" content="10"> -->
<html>
    <head> <title>Plant Monitor</title> </head>
    
    <body>
        <h1>Cactus Plant</h1>
        <h2>Moisture: {water}%</h2>
        <h2>Temp (C): {temp}c</h2>
        <h2>Humidity: {humidity}</h2>
    </body>
    <script type="text/javascript">
    setInterval('window.location.reload()', 10000);
</script>

</html>
"""
pm = PlantMonitor()
app = Microdot()

mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    w = pm.get_wetness()
    t = pm.get_temp()
    h = pm.get_humidity()
    response = html.format(water=w, temp=t, humidity=h)
    return response, {'Content-Type': 'text/html'}

app.run(port=80)
