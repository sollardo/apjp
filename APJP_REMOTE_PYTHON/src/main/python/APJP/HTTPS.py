from Crypto.Cipher import ARC4
from httplib import HTTPSConnection
from webob import Request
from webob import Response

APJP_KEY = ''
APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY = ['', '', '', '', '']
APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE = ['', '', '', '', '']

def application(environ, start_response):
  request = Request(environ)
  
  def http_response_body_generator():
    decipher = ARC4.new(APJP_KEY)
    
    http_request_header = ''
    
    while True:
      buffer = request.body_file.read(1)
      buffer_length = len(buffer)
      if buffer_length == 0:
        break
      http_request_header = http_request_header + decipher.decrypt(buffer)
      http_request_header_length = len(http_request_header)
      if http_request_header_length >= 4:
        if \
          http_request_header[http_request_header_length - 4] == '\r' and \
          http_request_header[http_request_header_length - 3] == '\n' and \
          http_request_header[http_request_header_length - 2] == '\r' and \
          http_request_header[http_request_header_length - 1] == '\n':
          break
    
    http_request_header_values = http_request_header.split('\r\n')
    http_request_header_values_length = len(http_request_header_values)
    
    http_request_address = ''
    http_request_port = 0
    http_request_headers = {}
    
    i = 1
    while i < http_request_header_values_length - 1:
      http_request_header_value1 = http_request_header_values[i]
      http_request_header_values1 = http_request_header_value1.split(': ')
      http_request_header_values1_length = len(http_request_header_values1)
      if http_request_header_values1_length == 2:
        http_request_header_value2 = http_request_header_values1[0]
        http_request_header_value3 = http_request_header_values1[1]
        if http_request_headers.get(http_request_header_value2) is None:
          http_request_headers[http_request_header_value2] = http_request_header_value3
        else:
          http_request_headers[http_request_header_value2] = http_request_headers[http_request_header_value2] + ', ' + http_request_header_value3
        if http_request_header_value2.upper() == 'Host'.upper():
          http_request_header1_values3 = http_request_header_value3.split(':')
          http_request_header1_values3_length = len(http_request_header1_values3)
          if http_request_header1_values3_length == 1:
            http_request_address = http_request_header1_values3[0]
            http_request_port = 443
          else:
            if http_request_header1_values3_length == 2:
              http_request_address = http_request_header1_values3[0]
              http_request_port = http_request_header1_values3[1]
      i = i + 1
    
    http_request_body = ''
    
    while True:
      buffer = request.body_file.read(5120)
      buffer_length = len(buffer)
      if buffer_length == 0:
        break
      http_request_body = http_request_body + decipher.decrypt(buffer)
    
    http_request_method = ''
    http_request_url = ''
    
    http_request_header_value1 = http_request_header_values[0]
    http_request_header_values1 = http_request_header_value1.split(' ')
    http_request_header_values1_length = len(http_request_header_values1)
    if http_request_header_values1_length == 3:
      http_request_method = http_request_header_values1[0]
      http_request_url = http_request_header_values1[1]
    
    https_connection = HTTPSConnection(http_request_address, http_request_port, None, None, False)
    https_connection.request(http_request_method, http_request_url, http_request_body, http_request_headers)
    http_response = https_connection.getresponse()
    
    cipher = ARC4.new(APJP_KEY)
    
    http_response_header = ''
    
    if http_response.version == 10:
      http_response_header = 'HTTP/1.0 ' + str(http_response.status) + '\r\n'
    else:
      http_response_header = 'HTTP/1.1 ' + str(http_response.status) + '\r\n'
    
    http_response_headers = http_response.getheaders()
    
    for (http_response_header_key, http_response_header_value) in http_response_headers:
      http_response_header = http_response_header + http_response_header_key + ': ' + http_response_header_value + '\r\n'
    
    http_response_header = http_response_header + '\r\n'
    
    yield cipher.encrypt(http_response_header)
    
    while True:
      buffer = http_response.read(5120)
      buffer_length = len(buffer)
      if buffer_length == 0:
        break
      yield cipher.encrypt(buffer)
    
    https_connection.close()
  
  http_response_headers = []
  
  i = 0
  while i < 5:
    if APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[i] != '':
      http_response_headers.append((APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[i], APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[i]))
    i = i + 1
  
  response = Response(None, None, http_response_headers, http_response_body_generator(), request)
  return response(environ, start_response)