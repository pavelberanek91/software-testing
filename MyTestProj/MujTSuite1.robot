*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
MujTCase1
    Open Browser    http://localhost:5000/    Chrome
    Close Browser
