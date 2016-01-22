import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://localhost/backwaters.mpeg'
li = xbmcgui.ListItem('BackWaters from TP-Streaming!', iconImage='icon.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

