# -*- coding: utf-8 -*-

#TV Box - by Christof Torres 2012 - 2014.

import urllib,urllib2,re,datetime,os.path,xbmcplugin,xbmcgui,xbmcaddon

from xml.dom import minidom

addon = xbmcaddon.Addon(id='plugin.video.tvbox')

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

root = 'https://raw.github.com/ChristofTorres/christofs-xbmc-addon-repository/master/plugin.video.tvbox/resources/data/countries.xml'

def COUNTRIES():
        xmlfile = urllib2.urlopen(root)
        error_server = 0
        if (os.path.exists(addon.getAddonInfo('path')+'/resources/data/'+root.split('/')[-1])):
                xmldocserver = minidom.parse(xmlfile)
        else:
                output = open(addon.getAddonInfo('path')+'/resources/data/'+root.split('/')[-1],'wb')
                output.write(xmlfile.read())
                output.close()
                xmldocserver = minidom.parse(addon.getAddonInfo('path')+'/resources/data/'+root.split('/')[-1])
                error_server = -1
        xmldoclocal = minidom.parse(addon.getAddonInfo('path')+'/resources/data/'+root.split('/')[-1])
        country_list_local = xmldoclocal.getElementsByTagName('country')
        index = -1; error_local = 0
        for country_server in xmldocserver.getElementsByTagName('country'):
                index += 1
                country_found = False
                for country_local in country_list_local:
                        if (country_server.attributes['name'].value == country_local.attributes['name'].value):
                                country_found = True
                if (index < len(country_list_local)):
                        timestamp_server = country_server.attributes['timestamp'].value.encode("utf-8")
                        timestamp_local = country_list_local[index].attributes['timestamp'].value.encode("utf-8")
                xml = country_server.attributes['xml'].value.encode("utf-8")
                if (not country_found or not os.path.exists(addon.getAddonInfo('path')+'/resources/data/'+xml.split('/')[-1]) or timestamp_server != timestamp_local):
                        xmlfile = urllib2.urlopen(xml)
                        output = open(addon.getAddonInfo('path')+'/resources/data/'+xml.split('/')[-1],'wb')
                        output.write(xmlfile.read())
                        output.close()
                        error_local = -1
                xml = addon.getAddonInfo('path')+'/resources/data/'+xml.split('/')[-1]
                name = '[B]'+country_server.attributes['name'].value.encode("utf-8")+'[/B] ('+str(len(minidom.parse(xml).getElementsByTagName('channel')))+')'
                thumbnail = addon.getAddonInfo('path')+'/resources/media/'+country_server.attributes['name'].value.encode("utf-8").lower()+'.jpg'
                addDir(name, xml, 1, thumbnail, 0)
        if (error_server != -1 and error_local == -1):
                xmlfile = urllib2.urlopen(root)
                output = open(addon.getAddonInfo('path')+'/resources/data/'+root.split('/')[-1],'wb')
                output.write(xmlfile.read())
                output.close()
                

def TVCHANNELS(xml):
        number = 0
        xmldoc = minidom.parse(xml)
        channel_list = xmldoc.getElementsByTagName('channel')
        for channel in channel_list:
                number += 1
                name = channel.attributes['name'].value.encode("utf-8")
                url = channel.attributes['url'].value.encode("utf-8")
                try:
                        if (addon.getSetting("epgsupport") == "true"):
<<<<<<< HEAD
<<<<<<< HEAD
                                epg = get_epg(channel.attributes['epg'].value.encode("utf-8"))
=======
                                if (url.find('megatv.to') == -1):
                                       epg = get_epg(channel.attributes['epg'].value.encode("utf-8"))
>>>>>>> db351165b4f8560a1d7d2e4c1798c7cdd493e65c
=======
                                if (url.find('megatv.to') == -1):
                                       epg = get_epg(channel.attributes['epg'].value.encode("utf-8"))
>>>>>>> FETCH_HEAD
                        else:
                                epg = ''
                except:
                        epg = 'No EPG Support'
                thumbnail = addon.getAddonInfo('path')+'/resources/media/'+name.lower()+'.jpg'
                addChannel(number, name, epg, url, 2, thumbnail, len(channel_list))


def TVSTREAMS(url,name,epg):
        urls = url.split(' ');
        number = 0
        for url in urls:
                number += 1
                try:
<<<<<<< HEAD
<<<<<<< HEAD
                        stream = "Stream "+str(number)
                        if (url.find('yourtv.to') != -1):
                                stream += ' [yourtv.to]' 
                                req = urllib2.Request('http://www.yourtv.to/js/app.js')
                                req.add_header('User-Agent', user_agent)
                                response = urllib2.urlopen(req)
                                link = response.read()
                                response.close()
                                server = re.compile('server = \'(.+?)\';').findall(link)[0]
                                pathname = url.replace('http://www.yourtv.to/online/live/fernsehen/stream/', '')
                                pathname = pathname.replace('.html', '')
                                token = re.compile('token = \'\?token=(.+?)\';').findall(link)[0]
                                rtmp = 'http://'+server+'/live/'+pathname+'/playlist.m3u8?token='+token
                        elif (url.find('live-stream.tv') != -1):
                                stream += ' [live-stream.tv]'
=======
                        if (url.find('www.live-stream.tv') != -1):
>>>>>>> db351165b4f8560a1d7d2e4c1798c7cdd493e65c
=======
                        if (url.find('www.live-stream.tv') != -1):
>>>>>>> FETCH_HEAD
                                req = urllib2.Request(url)
                                req.add_header('User-Agent', user_agent)
                                response = urllib2.urlopen(req)
                                link = response.read()
                                response.close()
                                flashvars = re.compile('file=(.+?)&amp;.+?streamer=(.+?)&amp;').findall(link)
                                for playpath, rtmp in flashvars:
                                        rtmp = rtmp+' swfUrl=http://stream.live-stream.tv/player.swf playpath='+playpath+' pageurl='+url+' live=true swfvfy=true'
                        elif (url.find('megatv.to') != -1):
<<<<<<< HEAD
<<<<<<< HEAD
                                stream += ' [megatv.to]'
=======
>>>>>>> db351165b4f8560a1d7d2e4c1798c7cdd493e65c
=======
>>>>>>> FETCH_HEAD
                                req = urllib2.Request(url)
                                req.add_header('User-Agent', user_agent)
                                response = urllib2.urlopen(req)
                                link = response.read()
                                response.close()
                                rtmp = re.compile('\'file\': \'(.+?)\'').findall(link)[0]
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> FETCH_HEAD
                                try:
                                        epg_title = re.compile('<center><font color=\'black\' size=\'4\' face=\'Jockey One\'>(.+?)<br>').findall(link)
                                        epg_time = re.compile('von (.+?) bis (.+?)</font><br>').findall(link)
                                        if (len(epg_title) > 0 and len(epg_time) > 0):
                                                epg = epg_title[0]+" "+epg_time[0][0]+" - "+epg_time[0][1]
                                        else:
                                                epg = get_epg(channel.attributes['epg'].value.encode("utf-8"))
                                except:
                                        epg = ''
<<<<<<< HEAD
>>>>>>> db351165b4f8560a1d7d2e4c1798c7cdd493e65c
=======
>>>>>>> FETCH_HEAD
                        else:
                                rtmp = url
                        thumbnail = addon.getAddonInfo('path')+'/resources/media/'+name.lower()+'.jpg'
                        addStream(stream, epg, rtmp, thumbnail, len(urls))
                except:
                        print "Unexpected Error: "+url


def get_epg(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()
        if (url.find('http://i.teleboy.ch') <> -1):
                now = link.split('<div id="showbox__0" class="showclass">')
                epg = re.compile('<p class="show_title"><a href="/programm/detail.php\?const_id=.+?">(.+?)</a>(.+?)<br /></p>').findall(now[1])
                title = epg[0][0].decode("iso-8859-1")
                title = title.encode("utf-8") 
                time = epg[0][1].decode("iso-8859-1")
                time = time.encode("utf-8")
        elif (url.find('tele.rtl.lu') <> -1):
                now = re.compile('<TR><TD class="highlight">(.+?)</TD><TD>&nbsp;<B><A HREF=".+?>(.+?)</A>.+?</B></TD></TR>').findall(link)
                epg = re.compile('<TR><TD class="highlight">(.+?)</TD><TD>&nbsp;.*?<A HREF=".*?>(.+?)</A>.+?</TD></TR>').findall(link)
                index = -1
                for epg_time, epg_title in epg:
                        index += 1
                        if (epg_time == now[0][0] and epg_title == now[0][1]):
                                index += 1
                                time = now[0][0]+' - '+epg[index][0]
                                title = now[0][1]
                                break
        elif (url.find('portalnacional.com.pt') <> -1):
                epg = re.compile('<div class="data">(.+?)</div><div class="titulo"><a href="(.+?)" title=".+?">(.+?)</a></div>').findall(link)
                now = datetime.datetime.utcnow()
                now_dt = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0, 0)
                for index in range(0, len(epg)-1):
                        epg[index] = (epg[index][0],epg[index+1][0],epg[index][2])
                for epg_start_time, epg_end_time, epg_title in epg:
                        epg_start_dt = datetime.datetime(now.year, now.month, now.day, int(epg_start_time.split(':')[0]), int(epg_start_time.split(':')[1]), 0, 0)
                        epg_end_dt = datetime.datetime(now.year, now.month, now.day, int(epg_end_time.split(':')[0]), int(epg_end_time.split(':')[1]), 0, 0)
                        if (epg_start_dt.time() <= now_dt.time() and epg_end_dt.time() >= now_dt.time()):
                                time = epg_start_time+' - '+epg_end_time
                                title = epg_title
                                break
        else:
                print 'Unknown EPG: '+url       
        return title+' '+time


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


def addStream(name,epg,url,iconimage,totalstreams):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": epg } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False,totalItems=totalstreams)
        return ok

def addChannel(number,name,epg,url,mode,iconimage,totalchannels):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&epg="+urllib.quote_plus(epg)
        ok=True
        if (number < 10):
                name = '[B]'+'  '+str(number)+' '+name+'[/B]'+'      '+epg
        else:
                name = '[B]'+str(number)+' '+name+'[/B]'+'      '+epg
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=totalchannels)
        return ok

def addDir(name,url,mode,iconimage,totalcountries):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=totalcountries)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None
epg=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        epg=urllib.unquote_plus(params["epg"])
except:
        pass

print "Mode: "+str(mode)
print "URL : "+str(url)
print "Name: "+str(name)
print "EPG: "+str(epg)

if mode==None or url==None or len(url)<1:
        print "COUNTRIES()"
        COUNTRIES()

elif mode==1:
        print "TVCHANNELS("+url+")"
        TVCHANNELS(url)

elif mode==2:
        print "TVSTREAMS("+url+","+name+","+epg+")"
        TVSTREAMS(url,name,epg)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
