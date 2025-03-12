import sys
import requests
import re
from loadJson import getMapleAPIKey

input = sys.stdin.readline

API_KEY = getMapleAPIKey()

headers = {
    "x-nxopen-api-key": API_KEY
}

def checkError(data):
    if 'error' in data:
        return "Exception occured : " + data['error']['message']
    
    return data


# 공지 목록 반환
def getNoticeList():
    url = "https://open.api.nexon.com/maplestory/v1/notice-event"
    data = requests.get(url, headers=headers).json()

    return checkError(data)['event_notice']


# requireNotice에 해당하는 공지 정보 반환
def getNoticeData(noticeList, requireNotice):
    # 받아온 정보 파싱
    noticeId = []
    for i in range(len(noticeList)):
        if requireNotice in noticeList[i]['title']:
            noticeId.append(noticeList[i]['notice_id'])
    
    if len(noticeId) == 0:
        return "일치하는 공지를 찾지 못했습니다."

    # 공지 정보 반환
    result = []
    for i in range(len(noticeId)):
        url = "https://open.api.nexon.com/maplestory/v1/notice-event/detail?notice_id=" + str(noticeId[i])
        data = requests.get(url, headers=headers).json()

        contents = data['contents']
        match = re.search(r'<img[^>]+src="([^"]+)"', contents)

        if match:
            result.append(match.group(1))
        else:
            print("링크를 찾지 못했습니다.")
            return None

    return result


def getEventData(eventName):
    noticeList = getNoticeList()
    noticeImageLink = getNoticeData(noticeList, eventName)
    
    return noticeImageLink
