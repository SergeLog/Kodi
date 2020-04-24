# -*- coding: utf-8 -*-
import sys
import xbmc
import urllib2
import urllib

if __name__ == '__main__':
	title = sys.listitem.getVideoInfoTag().getOriginalTitle()
	year = str(sys.listitem.getVideoInfoTag().getYear())
	
	if not title:
		title = sys.listitem.getVideoInfoTag().getTitle()
		if not title:
			xbmc.executebuiltin("Notification(\"Error ...\", \"%s\")" % 'Title is empty')
			sys.exit()
	xbmc.log('Downloading movie : %s (%s)' % (title, year))
	
	full_name = title+"/"+year
	if not year:
		full_name = title
	url_values = urllib.quote(full_name)
	url = 'http://localhost:8080/app/api/addsmall/'
	full_url = url + url_values
	response = urllib2.urlopen(full_url)
	
	xbmc.log('Sent request to url : %s' % full_url, xbmc.LOGDEBUG)
	
	message = "%s (%s)" % (title, year)
	xbmc.executebuiltin("Notification(\"Downloading ...\", \"%s\")" % message)
	
	response.close() 