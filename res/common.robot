*** Settings ***
Documentation   Common Keyword Definition
# Library    ../lib/test.py
Library    ../lib/Aha.py    WITH NAME    Aha_Lib

*** Variables ***
${browser_obj}        ${EMPTY}
${test_page}          https://www.earnaha.com/
${google_user}        %{GOOGLE_USERNAME}
${google_password}    %{GOOGLE_PASSWORD}
${date_to_change}     %{DATE_TO_CHANGE}

*** Keywords ***

Open Firfox To Web Page
    Aha_Lib.Open Firefox To Page    ${test_page}

Sign In To Existing Account With Google OAuth
    ${sign_in_result} =    Aha_Lib.Sign In With Google Oauth    ${google_user}    ${google_password}
    Set Global Variable    ${sign_in_result}

Validate Sign In
    # Should Be True    ${sign_in_result}
    Log To Console    ${sign_in_result}
    Should Contain    ${sign_in_result}    PASS

Sign Out Web Page
    ${sign_out_result} =    Aha_Lib.Sign Out
    Set Global Variable    ${sign_out_result}

Validate Sign Out
    Log To Console    ${sign_out_result}
    Should Contain    ${sign_out_result}    PASS

Chage Birthday Date
    ${chage_result} =    Change Birthday    ${date_to_change}
    Set Global Variable    ${chage_result}

Validate Change Date
    # Should Be True    ${chage_result}
    Log To Console    ${chage_result}
    Should Contain    ${chage_result}    PASS
