import json
def GetToken(NameKey:str):
    with open("D:\Seleção Prime Control\Atividade Pratica\Tasks\APIs\Clash Royale API\KEY\MyKeys.json","r") as file:Content = file.read();file.close();
    MyKeys = json.loads(Content)
    for key in MyKeys:
        if key["Name"] == NameKey:
            return key["Token"]
        return "Key Not Found"
        


# print(GetToken("Minha Nova Key 2"))