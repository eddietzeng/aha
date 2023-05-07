*** Settings ***
Documentation   AHA Sign In Tests

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Test Google OAuth Sign In
    Open Firfox To Web Page
    Sign In To Existing Account With Email
    Validate Sign In