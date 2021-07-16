import json
def SaveKey(Name:str,Description:str,Ip:str,Token:str):
    with open("D:\Seleção Prime Control\Atividade Pratica\Tasks\APIs\Clash Royale API\KEY\MyKeys.json","r") as file:Content = file.read();file.close();
    MyKeys = json.loads(Content)
    MyKeys.append({
        "Name":Name,
        "Description":Description,
        "IP":Ip,
        "Token":Token
    })
    with open("D:\Seleção Prime Control\Atividade Pratica\Tasks\APIs\Clash Royale API\KEY\MyKeys.json","w") as file:file.write(json.dumps(obj=MyKeys,indent=True));file.close()




# SaveKey(Name="Chave nova",Description="Esse cha exemplo",Ip="192.454.666.44",Token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjZkODYzZjg0LTNlZTMtNDAxYi1hZjE1LTNjMGI4NmMzODhjOSIsImlhdCI6MTYyNjI0MjU4MCwic3ViIjoiZGV2ZWxvcGVyLzgxMzAyN2MxLTZjMzUtYWU4Ny04ZTg5LWUwZDYzNmFhMDNkOSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjkuMjU0LjE3Ni45Il0sInR5cGUiOiJjbGllbnQifV19.uFurtVzjFz_JQ29I9tCvR_byVFKF1og9-uf9-13W3JM1I8ru2677cYT0LjeroNhNlQ9J9gv6EUULU8byzoQusQ")