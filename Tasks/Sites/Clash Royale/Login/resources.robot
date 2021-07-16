*** Settings ***
Documentation       Task com o objetivo Logar no site do Clash Royale API
Library             SeleniumLibrary


*** Keywords ***
#Login:
Abrir Browser Para Logar
    Open Browser    ${LOGIN URL}    ${BROWSER}  
    Wait Until Element Is Visible    //*[@id="email"]   

Inserir Username
    [Arguments]    ${username}
    Input Text    //*[@id="email"]    ${username}

Inserir Password
    [Arguments]    ${password}
    Input Text    //*[@id="password"]    ${password}

Clicar em Logar
    Click Button    //*[@id="content"]/div/div[2]/div/div/div/div/div/div/form/div[4]/button  

Verificar Se Logado
    Wait Until Element Is Visible    //*[@id="content"]/div/div[2]/div/div/div/div/div/h2/span[1]