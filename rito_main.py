import requests
import json

def bubbleSort(jawn,jawn2,jawn3,jawn4): 
    for i in range(len(jawn)):
        for j in range(i+1, len(jawn)):
            if jawn[j] > jawn[i]:
                jawn[j], jawn[i] = jawn[i], jawn[j]
                jawn2[j], jawn2[i] = jawn2[i], jawn2[j]
                jawn3[j], jawn3[i] = jawn3[i], jawn3[j]
                jawn4[j], jawn4[i] = jawn4[i], jawn4[j]
    return jawn, jawn2, jawn3, jawn4

def getJSON(url):
    response = requests.get(url)
    responseJSON = response.json()
    return responseJSON
                                                             
def getSumId(sum_name):
    url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + sum_name + '?api_key=3bbe1aa8-10d8-4862-8c68-b249f22e7b33'
    temp = (getJSON(url)) [sum_name]['id']
    return temp

def getSumLvl(sum_name):
    url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + sum_name + '?api_key=3bbe1aa8-10d8-4862-8c68-b249f22e7b33'
    temp = (getJSON(url)) [sum_name]['summonerLevel']
    return temp
    
def getSumRank(ssumID):
    url = 'https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/' + ssumID +'?api_key=3bbe1aa8-10d8-4862-8c68-b249f22e7b33'
    temp = (getJSON(url)) [ssumID][0]['tier']
    temp3 = ((getJSON(url)) [ssumID][0]['entries'])
    for i in range(len(temp3)):
        if (temp3[i]["playerOrTeamId"]) == ssumID:
            numm = i
            break
    temp2 = (getJSON(url)) [ssumID][0]['entries'][numm]['division']
    return temp,temp2
    
def getFavChamp(sumID, ssumID):
    url = 'https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + ssumID + '/ranked?season=SEASON2016&api_key=3bbe1aa8-10d8-4862-8c68-b249f22e7b33'
    response = requests.get(url)
    responseJSON = response.json()
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for x in range(len(responseJSON ['champions'])):
        list1.append(responseJSON ['champions'][x]['id'])
        list2.append(responseJSON['champions'][x]['stats']['totalSessionsPlayed'])
        list3.append(responseJSON['champions'][x]['stats']['totalSessionsWon'])
        list4.append(responseJSON['champions'][x]['stats']['totalSessionsLost'])
    list1, list2, list3, list4 = bubbleSort(list2,list1,list3,list4)
#    print list1,list2,list3,list4

    favChamp = list2[1]
    favChampWin = list3[1]
    favChampLoss = list4[1]
    
    url2 = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/' + str(favChamp) +'?locale=en_US&champData=recommended&api_key=3bbe1aa8-10d8-4862-8c68-b249f22e7b33'
    response = requests.get(url2)
    responseJSON = response.json()
    temp = responseJSON['recommended'][0]['champion']
    return temp,favChampWin,favChampLoss
    


def main():
    i = 0
    amount = 1
    #(int) (input("Enter the amount # of summs you wish to compare: "))

    while i < amount:
        sum_name = "jsimonsays"
        #(str) (input("Enter your sum. name: "))
        ssum_name = sum_name.lower()
        sumID = getSumId(ssum_name)
        ssumID = str(sumID)
        print ('Summoner ID:',sumID)
        sumLvl = getSumLvl(ssum_name)
        print ('Summoner Level:',sumLvl)
        sumRank,sumDiv = getSumRank(ssumID)
        print ('Summoner Rank:',sumRank,sumDiv)
        favChamp,favChampwin, favChamploss = getFavChamp(sumID, ssumID)
        print ('Most played Champ:',favChamp)
        print ('Wins:',favChampwin,'Losses:',favChamploss)
        i = i+1
    sleep(5)



if __name__ == "__main__":
    main()
