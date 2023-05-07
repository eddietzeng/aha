*** Settings ***
Documentation   AHA Edit Prodifle Tests

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Test Google OAuth Sign In
    Open Firfox To Web Page
    Sign In To Existing Account With Google OAuth
    Validate Sign In

Test Chage Birthday Date
    Chage Birthday Date
    Validate Change Date

Test Sign Out
    Sign Out Web Page
    Validate Sign Out