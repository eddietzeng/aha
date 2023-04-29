*** Settings ***
Documentation   Common Keyword Definition
Library    ../lib/helper.py

*** Variables ***
${year}         ${1972}
${month}        ${2}
${day}          ${23}

*** Keywords ***

Edit Date Of Birthday
    Change Birthday Date    ${web_driver}    ${year}    ${month}    ${day}
    ${change_result} =    Validate Birthday Date    ${web_driver}    ${year}    ${month}    ${day}
    Set Test Variable    ${change_result}

Validate Edit Date Of Birthday
    Should Be True    ${change_result}