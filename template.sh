standard () {
    local servicename="$1"
    local dirname="$2"
    cat template.yml | sed -e"s;SERVICENAME;${servicename};g" | sed -e"s;DIRNAME;${dirname};g" 
}

standard jarvis vendor/Jarvis/autogpts/autogpt/
standard the_agency_1  vendor/TheAgency/autogpts/autogpt/Dockerfile
standard the_agency_2  vendor/TheAgency/autogpts/ZEROAGPT_02/Dockerfile
standard the_agency_3  vendor/TheAgency/autogpts/ZEROAGPT_01/Dockerfile
standard the_agency_4  vendor/TheAgency/autogpts/ZEROAGPT_03/Dockerfile
standard mason_boom   vendor/MasonBoomPersonalAssistant/autogpts/autogpt/Dockerfile
standard mason_boom_pa  vendor/MasonBoomPersonalAssistant/autogpts/PersonalAssistant/Dockerfile
standard mason_boom_testgpt   vendor/MasonBoomPersonalAssistant/autogpts/testgpt/Dockerfile
standard swarms_of_sparta  vendor/Swarms-Of-Sparta/autogpts/autogpt/Dockerfile
standard mljar  vendor/mljar-agent/autogpts/autogpt/Dockerfile
