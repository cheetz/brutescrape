#!/usr/bin/python

#Secure Planet LLC

import urllib2
import re
import re
import os, sys

from collections import OrderedDict

banner_file = "brutescrape.banner"
def banner():
    global banner_file
    open_banner = open(banner_file, "r")
    for line in open_banner:
        print line.rstrip()
    open_banner.close()

def stripHTMLTags (html):
#Strip HTML tags from any string and transfrom special entities.
    text = html
 
#Apply rules in given order.
    rules = [
      { r'>\s+' : u'>'},                  # Remove spaces after a tag opens or closes.
      { r'\s+' : u' '},                   # Replace consecutive spaces.
      { r'\s*<br\s*/?>\s*' : u'\n'},      # Newline after a <br>.
      { r'</(div)\s*>\s*' : u'\n'},       # Newline after </p> and </div> and <h1/>.
      { r'</(p|h\d)\s*>\s*' : u'\n\n'},   # Newline after </p> and </div> and <h1/>.
      { r'<head>.*<\s*(/head|body)[^>]*>' : u'' },     # Remove <head> to </head>.
      { r'<a\s+href="([^"]+)"[^>]*>.*</a>' : r'\1' },  # Show links instead of texts.
      { r'[ \t]*<[^<]*?/?>' : u'' },            # Remove remaining tags.
      { r'^\s+' : u'' }                   # Remove spaces at the beginning.
    ]
 
    for rule in rules:
      for (k,v) in rule.items():
        try:
          regex = re.compile (k)
          text  = regex.sub (v, text)
        except:
          pass #Pass up whatever we don't find.
 
  #Replace special strings.
    special = {
      '&nbsp;' : ' ', '&amp;' : '&', '&quot;' : '"',
      '&lt;'   : '<', '&gt;'  : '>'
    }
 
    for (k,v) in special.items():
      text = text.replace (k, v)
 
    return text

banner()
#Create an empty list for generation logic.
y_arr = []

try:
    file_list = open('sites.scrape','r')
    sites = file_list.read().split(',')

except:
    banner()
    sys.exit()

for site in sites:
    try:
        site = site.strip()
        print "[*] Downloading Content For : " + site
        x_arr = []
        response = urllib2.urlopen(site)
        response.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0')]
        x = stripHTMLTags(response.read())
	#Replace junk found in our response
        x = x.replace('\n',' ')
        x = x.replace(',',' ')
        x = x.replace('.',' ')
        x = x.replace('/',' ')
        x = re.sub('[^A-Za-z0-9]+', ' ', x)
        x_arr = x.split(' ')
        for y in x_arr:
            y = y.strip()
            if y and (len(y) > 4):
              if ((y[0] == '2') and (y[1] == 'F')) or ((y[0] == '2') and (y[1] == '3')) or ((y[0] == '3') and (y[1] == 'F')) or ((y[0] == '3') and (y[1] == 'D')):
                y = y[2:]
              y_arr.append(y)
    except Exception as e:
        print "[*] Error: " + str(e)
        pass

y_arr_unique = OrderedDict.fromkeys(y_arr).keys()
print "[*] Processing List"
f_write = open("passwordList.txt","w")
for yy in y_arr_unique:
    if yy.strip().isdigit():
      pass
    else:
      #print yy.strip()
      f_write.write(yy.strip() + "\n")
f_write.close()
print "[*] Wordlist Generation Complete."
print "[*] Output Located: passwordList.txt"
print "[*] Total Count of Passwords >> " + str(len(y_arr_unique))
