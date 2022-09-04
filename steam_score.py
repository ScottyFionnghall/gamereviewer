import json
import requests
# get appid of entered game
def getAppID(game_name):
    f = open('response.json','r', encoding='utf-8')
    data = f.read().lower()
    f.close()
    dump = json.loads(data)
    appid = next((i for i, item in enumerate(dump['applist']['apps']) if item["name"] == game_name), None)
    # if game found return gameid, else return none
    if appid:
        appid = dump['applist']['apps'][appid]['appid']
        return appid
    else:
        return None
# get review score of entered game 
def getReviewScore(appid):
    # if game found return game score, if not, print('game not found') and return none
    if appid:
        request = requests.get('http://store.steampowered.com/appreviews/'+str(appid)+'?json=1')
        return(request.json()['query_summary'].get('review_score'))
    else:
        print('game not found')
        return(None)
# update game list
def updateGamesList():
    file = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
    f = open('response.json','w',encoding='utf-8')
    f.write(file.text)
    f.close()