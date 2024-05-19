from model import SentenceTransformer
import requests
import json

class BeyondChats:

    def __init__(self) -> None:
        
        self.__url = "https://devapi.beyondchats.com/api/get_message_with_sources"
        self.__response = requests.get(self.__url)
        self.__pageLinks = [{"page":i['label'],"url":i['url']} for i in self.__response.json()['data']['links'] if i['url'] != None]
        self.__lastPage = self.__response.json()['data']['last_page']

        self.__citations = {f"page{i}":{} for i in range(1,self.__lastPage + 1)}
        self.__currentPage = 1

    

    def getNewPageCitations(self):

        while (self.__currentPage <= 13):
            response = requests.get(self.__pageLinks[self.__currentPage - 1]['url']).json()['data']['data']
            
            currentPageCitationData = {}

            for i in range(len(response)):
                            
                mainStatement = response[i]['response']
                currentPageCitationData[mainStatement] = []
                # self.__citations[f"page{self.__currentPage}"]
                statementData = response[i]['source']
                statements = [j['context'] for j in response[i]['source']]
                mappings = SentenceTransformer().query(mainStatement,statements)
            
                for j in range(len(mappings)):
                    try:
                        if (mappings[j] > 0.5):
                            currentPageCitationData[mainStatement].append(statementData[j])
                    except:
                        print(self.__currentPage)
                        break
            
            self.__citations[f'page{self.__currentPage}'] = currentPageCitationData

            self.__currentPage += 1

        with open("results.json","w") as file:
            json.dump(self.__citations,file,indent=4)

        return self.__citations


    def getOldPageCitations(self):
        return json.load(open("results.json","r"))