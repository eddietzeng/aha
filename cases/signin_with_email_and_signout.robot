*** Settings ***
Documentation   AHA Sign In Test With Email And Sign Out

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Case 1-1 Test Email Sign In
    Open Firfox To Web Page
    Sign In To Existing Account With Email
    Validate Sign In

Case 2 Test Sign Out
    Sign Out Web Page
    Validate Sign Out
