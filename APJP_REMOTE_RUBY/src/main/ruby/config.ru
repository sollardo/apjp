require "./APJP/HTTP.rb"
require "./APJP/HTTPS.rb"
require "rack"

$APJP_KEY = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[0] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[0] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[1] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[1] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[2] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[2] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[3] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[3] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[4] = ""
$APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[4] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[0] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[0] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[1] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[1] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[2] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[2] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[3] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[3] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[4] = ""
$APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[4] = ""

application = Rack::URLMap.new(
  '/HTTP' => HTTP.new(),
  '/HTTPS' => HTTPS.new()
)

run application