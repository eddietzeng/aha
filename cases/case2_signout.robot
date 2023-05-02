*** Settings ***
Documentation   SingOut Tests

Resource        ../res/common.robot

*** Variables ***

*** Test Cases ***
Test Google OAuth Sign Out
    Open Firfox To Web Page
    Sign Out Web Page
    Validate Sign Out