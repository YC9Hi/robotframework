*** Settings ***
Documentation                               This is a basic test
Library                                     Selenium2Library
Library                                     OperatingSystem
Library                                     Process
Library                                     String
*** Variables ***
${browser}   chrome
${url}      https://store.hp.com/us/en
*** Test Cases ***
User can open home page
    [Documentation]                         Test if all the links at HP Store homepage are working
    run process     python      scrapeHP.py
    open browser                            ${url}      ${browser}
    Maximize Browser Window
    ${contents}=  Get File  HP_homepage_links.txt
    @{lines}=  Split to lines  ${contents}
    :FOR  ${line}  IN  @{lines}
    \   Log to console                          ${line}
#   We use command 'go to' instead of click link because click link by its href would have too many exceptions to catch
    \   go to                                   ${line}
#    \   click link                              xpath://a[@href='${line}']

*** Keywords ***
