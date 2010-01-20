#import os

#os.getenv("DISPLAY")
#os.putenv("DISPLAY", "sandman.ci.uiuc.edu:0.0")

import gobject, gnomekeyring

# The keyring needs to know the application name
if gobject.get_application_name() is None:
  gobject.set_application_name("offlineimap")
def keyring(user,host):
  keys = gnomekeyring.find_network_password_sync(user=user, server=host)
  # First one will do nicely thanks
  return keys[0]["password"]
