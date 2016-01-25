import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon(id='video.tp.streaming')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
videoURL = addon.getSetting('localvideo')

li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=videoURL)
li.setInfo(type='Video', infoLabels={ "Title": title })
li.setProperty('IsPlayable', 'true')

xbmc.Player().play(item=videoURL, listitem=li)

