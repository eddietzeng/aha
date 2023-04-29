*** Settings ***
Documentation   Common Keyword Definition
Library    ../lib/helper.py

*** Variables ***
${web_driver}         ${EMPTY}
${test_page}          https://www.earnaha.com/
${google_user}        eddiefree27@gmail.com
${google_password}    Ddong6lolcarousell

*** Keywords ***

Open Uc Chrome To Web Page
    ${web_driver} =    Open Uc Chrome To Page    ${test_page}
    Set Global Variable    ${web_driver}

Sign In To Existing Account With Google OAuth
    ${sign_in_result} =    Sign In With Google Oauth    ${web_driver}    ${google_user}    ${google_password}
    Set Test Variable    ${sign_in_result}

Validate Sign In
    Should Be True    ${sign_in_result}

Sign Out Web Page
    ${sign_out_result} =    Sign Out    ${web_driver}
    Set Test Variable    ${sign_out_result}

Validate Sign Out
    Should Be True    ${sign_out_result}

Test
    ${obj} =    Loging Page Obj    ${web_driver}
    ${obj}.test