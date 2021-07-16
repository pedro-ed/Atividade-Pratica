from KEY.GetKey import GetToken
from Locations.GetMyLocation import GetMyLocation
from Clans.Get import GetTagbyPart
from Clans.Members.Get import GetMembers
from Clans.Members.Export import ExportMembers

NameKey = "Minha Nova Key 2"
Pais = "BR"
clanName = "The resistance"
InitTag = "#9V2Y"
OutputPath = "D:\\Seleção Prime Control\\Atividade Pratica\\Process\\Criação_Chave\\"
NameReport = "Report"
Header = ["nome","level","troféus","papel"]


Token =  GetToken(NameKey)
LocationID = GetMyLocation(Pais,Token)
TagClan = GetTagbyPart(Name=clanName,Token=Token,InitTag=InitTag,IDLocation=LocationID)
Members = GetMembers(TagClan=TagClan,Token=Token)
ExportMembers(ListMembers=Members,OutputPath=OutputPath,NameReport=NameReport,Header=Header)



