*** Settings ***
Documentation   SingIn Tests

Resource        ../res/common.robot

*** Variables ***
${url}

*** Test Cases ***
Test Google OAuth Sign In(case 1 - googleauth)
    Open Uc Chrome To Web Page
    Sign In To Existing Account With Google OAuth
    Validate Sign In

Test Sign Out(case 2)
    Sign Out Web Page
    Validate Sign Out

