#!/usr/bin/python
# -*- coding: utf-8 -*-
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.config import cConfig
from resources.lib import logger
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.pluginHandler import cPluginHandler
import json,re


SITE_NAME = 'Mein_ddl.me'
URL_MAIN = 'http://de.ddl.me'
SITE_IDENTIFIER = 'mein_ddl_me'

URL_ALLE = URL_MAIN + '/moviez_00_0_1/'
URL_ACTION = URL_MAIN + '/moviez_02_0_1/'
URL_BLOCKBUSTER = URL_MAIN + '/moviez_25_0_1/'
URL_FAMILIE = URL_MAIN + '/moviez_08_0_1/'
URL_HORROR = URL_MAIN + '/moviez_11_0_1/'
URL_KRIEG = URL_MAIN + '/moviez_14_0_1/'
URL_ROMANTISCH = URL_MAIN + '/moviez_17_0_1/'
URL_THRILLER = URL_MAIN + '/moviez_21_0_1/'
URL_KINO = URL_MAIN + '/moviez_23_0_1/'
URL_ANIMATION = URL_MAIN + '/moviez_03_0_1/'
URL_DOKU = URL_MAIN + '/moviez_06_0_1/'
URL_FANTASY = URL_MAIN + '/moviez_09_0_1/'
URL_KLASSIKER = URL_MAIN + '/moviez_12_0_1/'
URL_MUSIK = URL_MAIN + '/moviez_15_0_1/'
URL_SCIFI = URL_MAIN + '/moviez_18_0_1/'
URL_WESTERN = URL_MAIN + '/moviez_22_0_1/'
URL_ABENTEUER = URL_MAIN + '/moviez_01_0_1/'
URL_BIOGRAFIE = URL_MAIN + '/moviez_04_0_1/'
URL_DRAMA = URL_MAIN + '/moviez_07_0_1/'
URL_GESCHICHTE = URL_MAIN + '/moviez_10_0_1/'
URL_KOMOEDIE = URL_MAIN + '/moviez_13_0_1/'
URL_MYSTERY = URL_MAIN + '/moviez_16_0_1/'
URL_SPORT = URL_MAIN + '/moviez_20_0_1/'

def load():
    oGui = cGui() 
    logger.info("Load %s" % SITE_NAME)
    params = ParameterHandler()
	
    params.setParam('sUrl', URL_ALLE)
    oGui.addFolder(cGuiElement('Alle', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_ACTION)
    oGui.addFolder(cGuiElement('Action', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_BLOCKBUSTER)
    oGui.addFolder(cGuiElement('Blockbuster', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_FAMILIE)
    oGui.addFolder(cGuiElement('Familie', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_HORROR)
    oGui.addFolder(cGuiElement('Horror', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_KRIEG)
    oGui.addFolder(cGuiElement('Krieg', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_ROMANTISCH)
    oGui.addFolder(cGuiElement('Romantisch', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_THRILLER)
    oGui.addFolder(cGuiElement('Thriller', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_KINO)
    oGui.addFolder(cGuiElement('Kino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_ANIMATION)
    oGui.addFolder(cGuiElement('Animation', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_DOKU)
    oGui.addFolder(cGuiElement('Doku', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_FANTASY)
    oGui.addFolder(cGuiElement('Fantasy', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_KLASSIKER)
    oGui.addFolder(cGuiElement('Klassiker', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MUSIK)
    oGui.addFolder(cGuiElement('Musik', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SCIFI)
    oGui.addFolder(cGuiElement('Sci-Fi', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_WESTERN)
    oGui.addFolder(cGuiElement('Western', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_ABENTEUER)
    oGui.addFolder(cGuiElement('Abenteuer', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_BIOGRAFIE)
    oGui.addFolder(cGuiElement('Biografie', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_DRAMA)
    oGui.addFolder(cGuiElement('Drama', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_GESCHICHTE)
    oGui.addFolder(cGuiElement('Geschichte', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_KOMOEDIE)
    oGui.addFolder(cGuiElement('Komödie', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MYSTERY)
    oGui.addFolder(cGuiElement('Mystery', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SPORT)
    oGui.addFolder(cGuiElement('Sport', SITE_IDENTIFIER, 'showEntries'), params)

    oGui.addFolder(cGuiElement('[COLOR red]Suche[/COLOR]', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory() 

def showEntries(entryUrl = False, sGui = False):

    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
	
    if not entryUrl: entryUrl = params.getValue('sUrl')
    iPage = int(params.getValue('page'))
    if iPage > 0:
        oRequest = cRequestHandler(entryUrl + '&per_page=' + str(iPage * 50))
    else:
        oRequest = cRequestHandler(entryUrl)
    sHtmlContent = oRequest.request()
	
    oGui.setView('movies')

    pattern = "class='iwrap type_0'.*?title='([^']+)' href='([^']+)'.*?<img alt='.*?' src='([^']+)'>"
    aResult = cParser().parse(sHtmlContent, pattern)
	
    oGui = cGui()
    _movieList(oGui, aResult)
	
    pattern = "<h1 ?.*>(.*)<\/h1>"
    bResult = cParser().parse(sHtmlContent, pattern)
	
    seitenInfo = str(bResult).replace("(True, ['","").replace("/"," - ").replace("#","").replace("'])"," - Next >>").strip()
    sitenUrl = str(entryUrl.split("_")[0] + '_' + entryUrl.split("_")[1] + '_' + entryUrl.split("_")[2] + '_' + entryUrl.split("_")[3].replace("/",""))
    seitenAddition = str(int(str(bResult).split("#")[1].split(" ")[0]) + 1)
    seitenMaxCount = int(str(bResult).split("von ")[1].split("'])")[0]) + 1

    if not int(seitenAddition) > int(seitenMaxCount):
        params.setParam('sUrl',sitenUrl  + '_' + seitenAddition + '/')
        oGui.addFolder(cGuiElement("[COLOR red]" + seitenInfo + "[/COLOR]", SITE_IDENTIFIER, 'showEntries'), params)
        oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False and sSearchText != ''):
        _searchMovieList(oGui, sSearchText)
    else:
        return
    oGui.setEndOfDirectory()

def _searchMovieList(oGui, sSearchString):
    searchUrl = URL_MAIN + '/search_99/?q=' 
    oRequest = cRequestHandler(searchUrl + sSearchString)
    content = oRequest.request()
    searchPattern = "class='iwrap type_0'.*?title='([^']+)' href='([^']+)'.*?<img alt='.*?' src='([^']+)'>"
    oParser = cParser()
    aResult = oParser.parse(content, searchPattern)
    if not aResult[0]:
        return
    params = ParameterHandler()
    function = 'getHosters'
    for title, link, img in aResult[1]:
        sLabel = title
        sTitle = sLabel
        sNextUrl = link
        params.setParam('siteUrl',sNextUrl)
        oGuiElement = cGuiElement(sTitle, SITE_IDENTIFIER, function)
        oGuiElement.setThumbnail(img)
        oGuiElement.setMediaType('movie')
        oGui.addFolder(oGuiElement, params, bIsFolder = False)

def _movieList(oGui, sresult):
    if not sresult[0]:
        return
    params = ParameterHandler()
    function = 'getHosters'
    for title, link, img in sresult[1]:
        sLabel = title
        sTitle = sLabel
        sNextUrl = link
        params.setParam('siteUrl',sNextUrl)
        oGuiElement = cGuiElement(sTitle, SITE_IDENTIFIER, function)
        oGuiElement.setThumbnail(img)
        oGuiElement.setMediaType('movie')
        oGui.addFolder(oGuiElement, params, bIsFolder = False) 
		
def getHosters():
    oParams = ParameterHandler()
    sUrl = oParams.getValue('siteUrl')
    oRequestHandler = cRequestHandler(URL_MAIN + sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\\','')
    sPattern = '"\d{1,2}","\w+",".*?","([^"]+)","\d+","stream"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern, ignoreCase = True)
    hosters = []
    sFunction='getHosterUrl'
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            hoster = {}
            hoster['link'] = aEntry
            temp = aEntry.split('//')
            temp = str(temp[-1]).split('/')
            temp = str(temp[0]).split('.')
            hoster['name'] = temp[-2]
            hosters.append(hoster)
        if len(hosters) > 0:
            hosters.append(sFunction)
    return hosters
   
def getHosterUrl(sStreamUrl = False):
    if not sStreamUrl:
        params = ParameterHandler()
        sStreamUrl = params.getValue('url')
    results = []
    result = {}
    result['streamUrl'] = sStreamUrl
    result['resolved'] = False
    results.append(result)
    return results