WRITE_MODE = "w"
READ_MODE = "r"
APPEND_MODE = "a"

class ProtobufFile:

    def __init__(self, filename, package_name, version):
        self.filename = filename
        self.package_name = package_name
        self.version = version
        self.create_header_file()

    def update_file(self, mode, contents):
        with open(self.filename, mode) as file:
            file.write(contents)

    def create_header_file(self):
        contents = f"syntax = 'proto{self.version}';\npackage {self.package_name};\n"
        self.update_file(WRITE_MODE, contents)

    def get_contents(self):
        with open(self.filename, "r") as file:
            return file.read()

    def add_enum(self, enum_name, values):
        index = 0
        contents = f"""\nenum {enum_name} """
        contents += "{\n"
        for value in values:
            contents += "\t" + value + " = " + str(index) + ";\n"
            index += 1
        contents += "}\n\n"
        self.update_file(APPEND_MODE, contents)

    def add_message(self, message_name, matrix):
        index = 1
        contents = "message " + message_name + " {\n"
        for r in matrix:
            contents += "\t"
            for c in r:
                contents += c + " "
            contents += "= " + str(index) + ";\n"
            index += 1
        contents += "}\n\n"
        self.update_file(APPEND_MODE, contents)

    def add_service(self, service_name):
        contents = "service " + service_name + " {\n}"
        self.update_file(APPEND_MODE, contents)

    def get_service_header(self, service_name):
        with open(self.filename, "r") as file:
            for line in file:
                if line.count("service " + service_name) == 1:
                    return line

    def add_rpc(self, service_name, rpc_name, rpc_input, rpc_output):
        # TODO: raise error if messages for rpc does not exist
        contents = self.get_service_header(service_name)
        if contents:
            file_contents = self.get_contents()
            service_header_start = file_contents.find(contents)
            to_replace = contents + "\trpc " + rpc_name + " (" + rpc_input + ") returns (" + rpc_output + ") {}"
            file_contents = file_contents[0:service_header_start] + to_replace
            file_contents += "\n}\n"
            self.update_file(WRITE_MODE, file_contents)
        else:
            raise RuntimeError("Could not find this service.")


