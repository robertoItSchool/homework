from http.server import HTTPServer, BaseHTTPRequestHandler
from flower_shop import FlowerShop, Tulip
import json

class FlowerRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    print('get')
    self.prepare_response()
    self.list_inventory()

  def prepare_response(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def list_inventory(self):
    inventory = FlowerShop().get_inventory()  # create the instance inline
    # call __dict__ on the flower objects in json.dumps
    inventory_json = json.dumps(inventory, default=lambda x: x.type)
    # encode the string to bytes
    to_bytes = inventory_json.encode()
    print(to_bytes)
    self.wfile.write(to_bytes)

  def do_POST(self):
    print('post')
    # extract the key content-length from headers
    length = self.headers.get('content-length')
    print(length)
    # read the request data
    data = self.rfile.read(int(length))
    decoded_data = json.loads(data.decode())
    if decoded_data['type'] == 'Tulip':
      flowers = [Tulip(decoded_data['colour'], decoded_data['number'])]
    FlowerShop().add_to_inventory(flowers)
    self.prepare_response()



server_address = ('localhost', 8000)
server = HTTPServer(server_address, FlowerRequestHandler)
server.serve_forever()

