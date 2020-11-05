from src.ProtobufFile import ProtobufFile
from robot.api.deco import keyword, library

@library
class ProtobufLibrary:
    ROBOT_LIBRARY_VERSION = '1.0.0'
    fileDict = dict()

    @keyword
    def create_protobuf_file(self, filename, package_name, version=3):
        temp = {filename: ProtobufFile(filename, package_name, version)}
        ProtobufLibrary.fileDict.update(temp)

    @keyword
    def get_protobuf_file_contents(self, filename):
        return ProtobufLibrary.fileDict.get(filename).get_contents()

    @keyword
    def add_enum(self, filename, enum_name, values):
        temp = ProtobufLibrary.fileDict.get(filename)
        temp.add_enum(enum_name, values)
        ProtobufLibrary.fileDict.update({filename: temp})

    @keyword
    def add_message(self, filename, message_name, values):
        temp = ProtobufLibrary.fileDict.get(filename)
        temp.add_message(message_name, values)
        ProtobufLibrary.fileDict.update({filename: temp})

    @keyword
    def create_service(self, filename, service_name):
        temp = ProtobufLibrary.fileDict.get(filename)
        temp.add_service(service_name)
        ProtobufLibrary.fileDict.update({filename: temp})

    @keyword
    def add_rpc(self, filename, service_name, rpc_name, rpc_input, rpc_output):
        with open("temp.txt", "w") as file:
            file.write(service_name)
            file.write(rpc_name)
            file.write(rpc_input)
            file.write(rpc_output)
        temp = ProtobufLibrary.fileDict.get(filename)
        temp.add_rpc(service_name, rpc_name, rpc_input, rpc_output)
        ProtobufLibrary.fileDict.update({filename: temp})
