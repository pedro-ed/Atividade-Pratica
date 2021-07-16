import os
from colorama import init,Fore,Back 
init(autoreset=True)
from robot.libraries.BuiltIn import BuiltIn
import datetime

def RegistreLog(msg,Process):
    directory = 'D:\\Seleção Prime Control\\Atividade Pratica\\Logs\\'+Process
    Path = directory+"\\LogProcess.log"
    if not os.path.exists(directory):os.makedirs(directory);open(Path,"w")
    with open(Path,"r+") as file:content = file.read()
    with open(Path,"w") as file:file.write(content+"\n"+msg)


def clear():
    os.system("CLS")

def hora():
    agora = datetime.datetime.now()
    return agora.strftime("%d/%m/%Y %H:%M:%S")

def LogError(msg,Process):
    LogMessageFile = f"[ERROR - {hora()} ] => {msg}"
    LogMessageConsole = Fore.LIGHTRED_EX+f"[ERROR - {hora()} ] => {msg}"+Fore.RESET
    BuiltIn().log_to_console(f"\n\r\t{LogMessageConsole}")
    RegistreLog(LogMessageFile,Process)

def LogInfo(msg,Process):
    LogMessageFile = f"[INFO - {hora()} ] => {msg}"
    LogMessageConsole = Fore.LIGHTBLUE_EX+f"[INFO - {hora()} ] => {msg}"+Fore.RESET
    BuiltIn().log_to_console(f"\n\r\t{LogMessageConsole}")
    RegistreLog(LogMessageFile,Process)






LogError("Mensagem de Error","teste")


