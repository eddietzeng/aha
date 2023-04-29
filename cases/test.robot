*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Earnaha Website and Login with Google
    Open Browser    https://www.earnaha.com/    chrome
    Wait Until Page Contains    Log In
    Click Element    xpath=//a[@href='https://app.earnaha.com/api/auth/login']
    Wait Until Page Contains    Continue with Google
    Click Element    xpath=//span[text()='Continue with Google']
    Input Text    xpath=//input[@type='email']    eddiefree27@gmail.com
    Click Element    xpath=//span[text()='Next' or text()='繼續' or text()='下一步']
    Input Text    xpath=//input[@type='password']    Ddong6lolcaoursell
    Click Element    xpath=//button[@type='submit']
    Wait Until Page Contains    Continue