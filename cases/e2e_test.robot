*** Settings ***
Documentation   AHA End to End Tests

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Case 1: Test Google OAuth Sign In
    Open Firfox To Web Page
    Sign In To Existing Account With Google OAuth
    Validate Sign In

Case 3: Test Chage Birthday Date
    Chage Birthday Date
    Validate Change Date

Case 2: Test Sign Out
    Sign Out Web Page
    Validate Sign Out