*** Settings ***
Documentation   AHA Sign In Tests With Google Oauth And Sign Out

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Case 1-2 Test Google OAuth Sign In
    Open Firfox To Web Page
    Sign In To Existing Account With Google OAuth
    Validate Sign In

Case 2 Test Sign Out
    Sign Out Web Page
    Validate Sign Out
