*** Settings ***
Library    ProtobufLibrary

*** Variables ***
#field variable     flag_1      flag_2      type    name
@{FIELD_1}          optional    repeated    string  names
@{FIELD_2}          repeated    int32   timeout
@{MESSAGE}          ${FIELD_1}  ${FIELD_2}
*** Test Cases ***
My First Test
    create protobuf file    hello.proto     myfile
    get protobuf file contents  hello.proto
    ${ENUM_VALUES}  Create List    FIRST_VALUE     SECOND_VALUE  THIRD_VALUE
    add enum  hello.proto    MyEnums    ${ENUM_VALUES}
    add message     hello.proto   my_message    ${MESSAGE}
    create service     hello.proto   my_service
    create service     hello.proto   my_other_service
    add rpc         hello.proto   my_servdice    MyRPC   MyInput     MyOutput
