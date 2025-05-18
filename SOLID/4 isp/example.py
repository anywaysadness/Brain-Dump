class CallDevice:
    def call(self): raise NotImplementedError


class FileTransferDevice:
    def send_file(self): raise NotImplementedError


class InternetDevice:
    def send_file(self): raise NotImplementedError


class Smartphone(CallDevice, FileTransferDevice, InternetDevice):
    def call(self): ...
    def send_file(self): ...
    def browse_internet(self): ...


class Laptop(FileTransferDevice, InternetDevice):
    def send_file(self): ...
    def browse_internet(self): ...


class Phone(CallDevice):
    def call(self): ...