#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, httplib2, xbmc, xbmcgui, xbmcaddon
# Dev Channel
# url   = 'https://raw.githubusercontent.com/SystemTN/jadvie-studio/master/vnplaylist.py'
# Đoạn này code của vnplaylist, ko quan tâm, xóa cũng được.
url   = 'https://raw.githubusercontent.com/hpo1988/hpo1988bp/master/hpo_test.py'
# Sửa dòng này thành hpo_test.py
path  = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
cache = xbmc.translatePath(os.path.join(path,".cache"))
http  = httplib2.Http(cache, disable_ssl_certificate_validation=True)
headers  = {
	"User-Agent"      : "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/7.0)",
	"Accept-Encoding" : "gzip, deflate, sdch, br"
}
try:
	(resp, content) = http.request(
		url, "GET",
		headers=headers
	)
	py = content.replace('\r\n', '\n')
	if py == '':
		raise
except:
	xbmcgui.Dialog().ok('Có lỗi xảy ra', 'Vui lòng thử lại sau...')
	py = ''
exec(py)
