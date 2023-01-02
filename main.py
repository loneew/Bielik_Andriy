from enum import Enum
import dropbox
import os


class MethodType(Enum):
    UPLOAD = 0,
    GETFILEMETADATA = 1,
    DELETEFILE = 2


class Method:
    def __init__(self, access_token, dbx_path, comp_path):
        self.at = access_token
        self.cp = comp_path
        self.dp = dbx_path
        self.dbx = dropbox.Dropbox(self.at)


class Upload(Method):
    def __init__(self, at, dp, cp):
        super().__init__(at, dp, cp)
        with open(self.cp, 'rb') as file:
            self.dbx.files_upload(file.read(), self.dp)
        print(" Your file was uploaded.\n")


class GetFileMetadata(Method):
    def __init__(self, at, dp, cp):
        super().__init__(at, dp, cp)
        res = self.dbx.files_get_metadata(self.dp)
        print(" Metadata:\nName - " + res.name + "\npath - " + res.path_display + "\nsize - " + str(res.size))
        print("server_modified - " + str(res.server_modified) + "\nid - " + res.id[3:] + "\n")


class DeleteFile(Method):
    def __init__(self, at, dp, cp):
        super().__init__(at, dp, cp)
        self.dbx = dropbox.Dropbox(self.at)
        self.dbx.files_delete_v2(self.dp)
        print(" File was deleted.")


def func(method_type: MethodType, access_token, dbx_path, comp_path) -> Method:
    factory_dict = {
        MethodType.UPLOAD: Upload,
        MethodType.GETFILEMETADATA: GetFileMetadata,
        MethodType.DELETEFILE: DeleteFile
    }
    return factory_dict[method_type](access_token, dbx_path, comp_path)


class Test:
    def __init__(self):
        self.access_token = input("Enter your DB access token: ")
        self.dbx_path = '/Antoine.jpg'
        self.rel_path = os.path.dirname(__file__)
        self.comp_path = os.path.join(self.rel_path, 'ph\Antoine.jpg')

    def run_test(self):
        try:
            for method in MethodType:
                func(method, self.access_token, self.dbx_path, self.comp_path)
        except:
            print("\nSomething went wrong (\nPerhaps, your access token is invalid.")


def main():
    test1 = Test()
    test1.run_test()


if __name__ == "__main__":
    main()
