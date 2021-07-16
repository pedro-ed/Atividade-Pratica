*** Settings ***
Documentation       Task com o objetivo Criiar uma nova Key no site do Clash Royale API
Library             SeleniumLibrary

*** Keywords ***

Acessar Formulario de nova Key
    Go To    https://developer.clashroyale.com/#/new-key
    Wait Until Element Is Visible    //*[@id="content"]/div/div[2]/div/div/section/div/div/div[1]/h2
    
Pegar IP Local
    ${IP}             GetMyIP
    [Return]          ${IP}

Inserir KEY NAME
    [Arguments]    ${KEY NAME}
    Input Text    //*[@id="name"]    ${KEY NAME}

Inserir KEY DESCRIPTION
    [Arguments]    ${KEY DESCRIPTION}
    Input Text    //*[@id="description"]    ${KEY DESCRIPTION}

Inserir IP ADDRESSES
    [Arguments]    ${IP ADDRESSES}
    Input Text    //*[@id="range-0"]    ${IP ADDRESSES}

Clicar em Create Key
    Click Button    //*[@id="content"]/div/div[2]/div/div/section/div/div/div[2]/form/div[5]/button

Acessar Key Criada
    [Arguments]    ${KEY NAME}
    Wait Until Element Is Visible    xpath=//h4[contains(.,"${KEY NAME}")]
    Click Element                    xpath=//h4[contains(.,"${KEY NAME}")]

Pegar Token da Key
    Wait Until Element Is Visible    //*[@id="content"]/div/div[2]/div/div/section/div/div/div[2]/form/div[1]/div
    ${TOKEN}  Get Text               //*[@id="content"]/div/div[2]/div/div/section/div/div/div[2]/form/div[1]/div
    [Return]                         ${TOKEN}

Salvar Key
    [Arguments]    ${KEY NAME}    ${KEY DESCRIPTION}    ${IP}    ${KEY TOKEN}
    SaveKey        ${KEY NAME}    ${KEY DESCRIPTION}    ${IP}    ${KEY TOKEN}


