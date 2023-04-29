*** Settings ***
Documentation   SingOut Tests

Resource        ../res/common.robot

*** Variables ***

*** Test Cases ***
Test Google OAuth Sign In
    Sign Out
    Validate Sign Out

