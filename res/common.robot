*** Settings ***
Documentation   Common Keyword Definition
# Library    ../lib/test.py
Library    ../lib/Aha.py    WITH NAME    Aha_Lib

*** Variables ***
${browser_obj}        ${EMPTY}
${test_page}          https://www.earnaha.com/
${google_user}        eddiefree27@gmail.com
${google_password}    Ddong6lolcarousell

*** Keywords ***

Open Firfox To Web Page
    Aha_Lib.Open Firefox To Page    ${test_page}

Sign In To Existing Account With Google OAuth
    ${sign_in_result} =    Aha_Lib.Sign In With Google Oauth    ${google_user}    ${google_password}
    Set Global Variable    ${sign_in_result}

Validate Sign In
    Should Be True    ${sign_in_result}

Sign Out Web Page
    ${sign_out_result} =    Aha_Lib.Sign Out
    Set Global Variable    ${sign_out_result}

Validate Sign Out
    Should Be True    ${sign_out_result}
