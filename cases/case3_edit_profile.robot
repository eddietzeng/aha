*** Settings ***
Documentation   SingIn Tests

Resource        ../res/common.robot
Resource        ../res/myprofile.robot

*** Variables ***

*** Test Cases ***
Test Google OAuth Sign In
    Open Uc Chrome To Web Page
    Sign In To Existing Account With Google OAuth
    Validate Sign In

Test Edit Date Of Birthday
    Edit Date Of Birthday
    Validate Edit Date Of Birthday