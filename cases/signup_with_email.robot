*** Settings ***
Documentation   AHA Sign Up Test

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Case 4 Test Email Sign Up
    Open Firfox To Web Page
    Sign Up With Email
    Validate Sign Up

