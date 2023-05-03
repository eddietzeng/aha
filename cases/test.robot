*** Variables ***
${MY_VARIABLE}     %{MY_ENV_VAR}
${MY_VARIABLE2}    %{TEST2}

*** Test Cases ***
My Test Case
    Log To Console    The value of MY_VARIABLE is: ${MY_VARIABLE}
    Log To Console    The value of MY_VARIABLE is: ${MY_VARIABLE2}