import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(os.sep, 'tmp', 'server_mami', 'mako_modules')
log_dir = os.path.join(os.sep, 'tmp', 'server_mami', 'log')
data_file = os.path.join(current_dir, 'static', 'data', 'features.json')
firmware_dir = os.path.join(current_dir, 'db', 'firmware', 'molen_counter')
authentication_dir = os.path.join(current_dir, 'db', 'authentication')

# value = 'esp8266_0.0.6.bin'
firmware_pattern = r'^(.*?)_([0-9]+)\.([0-9]+)\.([0-9]+)\.bin'

cache_delay = 5  # in minutes
sse_timeout = 5000  # in seconds
