*** Settings ***
Library    ProtobufLibrary

*** Variables ***
#field variable     flag_1      flag_2      type    name
@{FIELD_1}          optional    repeated    string  names
@{FIELD_2}          repeated    int32   timeout
@{MESSAGE}          ${FIELD_1}  ${FIELD_2}
*** Test Cases ***
My First Test
    log to console  1
    create protobuf file    hello.proto     myfile
    log to console  2
    get protobuf file contents  hello.proto
    log to console  3
    ${ENUM_VALUES}  Create List    FIRST_VALUE     SECOND_VALUE  THIRD_VALUE
    log to console  4
    add enum  hello.proto    MyEnums    ${ENUM_VALUES}
    log to console  5
    log to console  ${MESSAGE}
    add message     hello.proto   my_message    ${MESSAGE}
    log to console  6
    create service     hello.proto   my_service
    log to console  7
    add rpc         hello.proto   my_service    MyRPC   MyInput     MyOutput
