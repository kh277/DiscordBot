import json

def getBotToken():
    with open('./parameter.json', 'r') as file:
        jsonData = json.load(file)
    
    file.close()
    return jsonData['DISCORD_BOT_TOKEN']


def getBotApplicationID():
    with open('./parameter.json', 'r') as file:
        jsonData = json.load(file)
    
    file.close()
    return jsonData['DISCORD_BOT_APPLICATION_ID']


def getMapleAPIKey():
    with open('./parameter.json', 'r') as file:
        jsonData = json.load(file)
    
    file.close()
    return jsonData['MAPLE_API_KEY']