*** Settings ***
Documentation   AHA Edit Prodifle Tests

Resource          ../res/common.robot
Suite Teardown    Close Page And Browser

*** Variables ***

*** Test Cases ***
Test Email Sign Up
    Open Firfox To Web Page
    Sign Up With Email
    Validate Sign Up

