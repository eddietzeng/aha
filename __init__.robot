*** Settings ***
Library    lib/helper.py

Suite Setup    INITIAL WEBDRIVER


*** Variables ***
${page}    https://www.earnaha.com/


*** Keywords ***
INITIAL WEBDRIVER
    Log To Console    ${page}
    ${web_driver} =    Open Uc Chrome To Page  
    Set Global Variable    ${WEB_DRIVER}    ${web_driver}
    ${CONFIG}    Parse XML    ${CURDIR}/../../config/config.xml
    Log To Console    ${CURDIR}

    ${SERVERS}    Get Element    ${CONFIG}    servers
    ${DB}    Get Element    ${SERVERS}    *[@name="nsppublic_prerel"]
    Set Global Variable    ${DB_NAME}    ${DB.attrib['name']}
    Set Global Variable    ${DB_IP}    ${DB.attrib['ip']}
    Set Global Variable    ${DB_USER}    ${DB.attrib['username']}
    Set Global Variable    ${DB_PASSWORD}    ${DB.attrib['password']}
    Set Global Variable    ${NCDE_NUMBER}    ${DB.attrib['ncde']}
    Set Global Variable    ${NCDE_PASS}    ${DB.attrib['pass']}

    ${SERVERS}    Get Element    ${CONFIG}    servers
    ${MEDIA_SERVER}    Get Element    ${SERVERS}    *[@name="media_server"]
    Set Global Variable    ${MEDIA_SERVER_NAME}    ${MEDIA_SERVER.attrib['name']}
    Set Global Variable    ${MEDIA_SERVER_IP}    ${MEDIA_SERVER.attrib['ip']}
    Set Global Variable    ${MEDIA_SERVER_USER}    ${MEDIA_SERVER.attrib['username']}
    Set Global Variable    ${MEDIA_SERVER_PASSWORD}    ${MEDIA_SERVER.attrib['password']}
    Set Global Variable    ${MEDIA_FOLDER}    ${MEDIA_SERVER.attrib['folder']}
    ${MEDIA_HOST}    Catenate    SEPARATOR=    http://    ${MEDIA_SERVER_IP}    /    ${MEDIA_FOLDER}
    Set Global Variable    ${MEDIA_HOST}

Get info from suite name
    Should Not Be Empty    ${TEST_SET_NAME}    msg="Test_Set_Name cannot be empty."
    @{TESTCOND}    Split String    ${TEST_SET_NAME}    _
    Set Global Variable    ${OS}    @{TESTCOND}[0]
    Run Keyword If    '${suts.sut.sys_hostname}' == '${Empty}'    Set SUT Hostname    @{TESTCOND}[1]
    @{NIC_LIST}    Split String    @{TESTCOND}[2]    \#
    Set Global Variable    @{NIC_LIST}

    ${CONFIG}    Parse XML    ${CURDIR}/../../config/config.xml
    Log To Console    ${CURDIR}
    ${SUTS}    Get Element    ${CONFIG}    suts
    ${SUT}    Get Element    ${SUTS}    *[@sys_hostname='${suts.sut.sys_hostname}']
    Set Suite Variable    ${CONFIG}
    Set Global Variable    ${suts.sut.ilo_ip}    ${sut.attrib['ilo_ip']}
    Set Global Variable    ${suts.sut.ilo_user}    ${sut.attrib['ilo_username']}
    Set Global Variable    ${suts.sut.ilo_password}    ${sut.attrib['ilo_password']}
    Set Global Variable    ${suts.sut.sys_ip}    ${sut.attrib['sys_ip']}
    Set Global Variable    ${suts.sut.sys_username}    ${sut.attrib['sys_username']}
    Set Global Variable    ${suts.sut.sys_password}    ${sut.attrib['sys_password']}
    Set Global Variable    ${suts.sut.sys_hostname}    ${sut.attrib['sys_hostname']}

Get info from cirrus
    @{NIC_LIST}    Split String    ${CIRRUS_STAGE_SUT_DATA['nic_list']}    \#
    Set Global Variable    @{NIC_LIST}
    Set Global Variable    ${suts.sut.ilo_ip}           ${CIRRUS_STAGE_SUT_DATA['ilo_ip']}
    Set Global Variable    ${suts.sut.ilo_user}         ${CIRRUS_STAGE_SUT_DATA['ilo_user']}
    Set Global Variable    ${suts.sut.ilo_password}     ${CIRRUS_STAGE_SUT_DATA['ilo_password']}
    Set Global Variable    ${suts.sut.sys_ip}           ${CIRRUS_STAGE_SUT_DATA['sys_ip']}
    Set Global Variable    ${suts.sut.sys_username}     ${CIRRUS_STAGE_SUT_DATA['sys_username']}
    Set Global Variable    ${suts.sut.sys_password}     ${CIRRUS_STAGE_SUT_DATA['sys_password']}
    Set Global Variable    ${suts.sut.sys_hostname}     ${CIRRUS_STAGE_SUT_DATA['name']}
    Set Global Variable    ${OS}                        ${CIRRUS_STAGE_SUT_DATA['os_type']}

Set SUT Hostname
    [Arguments]    ${hostname}
    Set Global Variable    ${suts.sut.sys_hostname}    ${hostname}