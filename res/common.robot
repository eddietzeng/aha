*** Settings ***
Documentation   Common Keyword Definition
# Library    ../lib/test.py
Library    ../lib/Aha.py    WITH NAME    Aha_Lib

*** Variables ***
${browser_obj}          ${EMPTY}
${test_page}            https://www.earnaha.com/
${google_user}          %{GOOGLE_USERNAME}
${google_password}      %{GOOGLE_PASSWORD}
${login_user}           %{EMAIL_USERNAME}
${login_pssword}        %{EMAIL_PASSWORD}
${date_to_change}       %{DATE_TO_CHANGE}
${mailslurp_api_key}    %{MAILSLURP_API_KEY}
${sign_out_result}      ${False}
${chage_result}         ${False}

*** Keywords ***

Open Firfox To Web Page
    Aha_Lib.Open Firefox To Page    ${test_page}

Sign In To Existing Account With Google OAuth
    ${sign_in_result} =    Aha_Lib.Sign In With Google Oauth    ${google_user}    ${google_password}
    Set Global Variable    ${sign_in_result}

Sign In To Existing Account With Email
    ${sign_in_result} =    Aha_Lib.Sign In With Email    ${login_user}    ${login_pssword}
    Set Global Variable    ${sign_in_result}

Validate Sign In
    Should Be True    ${sign_in_result}

Sign Up With Email
    ${sign_up_result} =    Aha_Lib.Sign Up With Email    ${mailslurp_api_key}
    Set Global Variable    ${sign_up_result}

Validate Sign Up
    Should Be True    ${sign_up_result}

Sign Out Web Page
    ${sign_out_result} =    Run Keyword If    "${sign_in_result}" == "${True}"    Aha_Lib.Sign Out
    Set Global Variable    ${sign_out_result}

Validate Sign Out
    Should Be True    ${sign_out_result}

Chage Birthday Date
    ${chage_result} =    Run Keyword If    "${sign_in_result}" == "${True}"    Change Birthday    ${date_to_change}
    Set Global Variable    ${chage_result}

Validate Change Date
    Should Be True    ${chage_result}

Close Page And Browser
    Aha_Lib.Close

