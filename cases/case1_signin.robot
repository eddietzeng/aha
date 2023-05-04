*** Settings ***
Documentation   SingIn Tests

Resource        ../res/common.robot

*** Variables ***

*** Test Cases ***
Test
    Log To Console     ${google_user}
    Log To Console     ${google_password}
    
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
