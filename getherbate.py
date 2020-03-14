#!/usr/bin/env python2

import getopt, sys
import json
import urllib2

from resources.lib import VLC
from resources.lib import Config


def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "m:c", ["model=","vlc"])
  except getopt.GetoptError as err:
    print str(err)
    sys.exit(2)
  vlccli = False
  for option, value in opts:
    if option in ("-m", "--model"):
      MODEL = value
    elif option in ("-c", "--vlc"):
      vlccli = True
    else:
      assert False, "unhandled option"

  argh = {}
  url = "%s/%s/" % (Config.CHATURBATE_API, MODEL)
  request = urllib2.Request(url)
  request.add_header('User-Agent', Config.USER_AGENT)
  data = urllib2.urlopen(request).read()
  argh = data.encode('utf-8')
  json_data = json.loads(argh)
  if vlccli == True:
    print "%s" % (json_data["hls_source"])
  else:
    print "%s:%s" % (json_data["room_status"], json_data["hls_source"])
  #instance = VLC.Instance()

if __name__ == "__main__":
    main()


# vim: ts=2 sw=2 noai expandtab
