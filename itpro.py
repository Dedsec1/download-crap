from __future__ import unicode_literals
import subprocess
import dryscrape
import sys
from shell import ex

if 'linux' in sys.platform:
    # start xvfb in case no X is running. Make sure xvfb 
    # is installed, otherwise this won't work!
    dryscrape.start_xvfb()

search_term = 'dryscrape'

# set up a web scraping session
sess = dryscrape.Session(base_url = sys.argv[1])

# we don't need images
sess.set_attribute('auto_load_images', False)

url = sys.argv[1]
sess.visit(url)

# extract all links
for link in sess.xpath('//iframe[@ng-src]'):
  print(link['ng-src'])
  url = (link['ng-src'])
  print url

bashCommand = 'youtube-dl -v'.encode('utf-8'), url.encode('utf-8'), '--referer http://itpro.tv'.encode('utf-8')
bashCommand = " ".join(bashCommand)
print bashCommand
ex(bashCommand).stdout()
#output = subprocess.check_output(['bash','-c', bashCommand])
