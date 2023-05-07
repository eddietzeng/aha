*** Settings ***
Documentation   AHA Sign Out Test

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Test Google OAuth Sign In
    Open Firfox To Web Page
    Sign In To Existing Account With Google OAuth
    Validate Sign In

Test Sign Out
    Sign Out Web Page
    Validate Sign Out