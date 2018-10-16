import urllib2
response = urllib2.urlopen('http://www.hamicogroup.vn/wp-login.php')
html = response.read()