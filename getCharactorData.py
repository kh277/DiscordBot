# 메이플 API로 캐릭터의 정보를 받아오는 기능 수행

import requests
from loadJson import getMapleAPIKey

API_KEY = getMapleAPIKey()

headers = {
    "x-nxopen-api-key": API_KEY
}

def checkError(data):
    if 'error' in data:
        print("Exception occured : " + data['error']['message'])
        return None
    
    return data


# 캐릭터의 OCID 정보 반환
def getOCID(_characterName):
    ocidUrl = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + _characterName
    data = checkError(requests.get(ocidUrl, headers=headers).json())

    return str(checkError(data)['ocid'])


# OCID로 캐릭터의 정보 반환
def getCharacterData(_ocid):
    ocidUrl = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + _ocid
    data = checkError(requests.get(ocidUrl, headers=headers).json())

    return [data['character_level'], data['character_exp_rate']]


def getCharacterExp(characterName):
    try:
        ocid = getOCID(characterName)
        characterData = getCharacterData(ocid)
    except:
        return None

    return characterData
