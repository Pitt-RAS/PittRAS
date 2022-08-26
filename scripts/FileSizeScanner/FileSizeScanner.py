import os
import glob

class FileSizeScanner:

    def __init__(self):
        self.file_path=""
        self.file_size_limit = 100000  # units: bytes
        self.files = []
        self.failed_files = []

        self.__get_input()
        # self.__test_human_readable_size()

    def __get_input(self):

        while True:
            self.file_path = input("Type in the full file path:\n")
            if not os.path.exists(self.file_path):
                print("Not a valid path, please try again.")
            else:
                break
        
        print("")

        file_size = input("Please enter file size threshold. Any files above this threshold will be flagged:\n")
        try:
            self.file_size_limit = int(file_size)
        except:
            print("Could not convert to int. Using default value specified in program (100000 bytes).")

        print()

    def __get_human_readable_size(self, file_size) -> str:
        unit = ""
        if file_size >= 1073741824:
            file_size /= 1073741824
            unit = "GB"
        elif file_size >= 1048576:
            file_size /= 1048576
            unit = "MB"
        elif file_size >= 1024:
            file_size /= 1024
            unit = "KB"
        else:
            unit = "B"
        return (str(round(file_size, 2)) + " " + unit)

    def __test_human_readable_size(self):
        print(self.__get_human_readable_size(1))
        print(self.__get_human_readable_size(10))
        print(self.__get_human_readable_size(111))
        print(self.__get_human_readable_size(1048576))
        print(self.__get_human_readable_size(1024))
        

    def scan_files(self):
        files_flagged_count = 0
        self.files = glob.glob(self.file_path + "/**/*", recursive = True)
        for file in self.files:
            os_size = os.path.getsize(file)
            size = self.__get_human_readable_size(os_size)
            if os_size == 0:
                self.failed_files.append(file)
            if os_size >= self.file_size_limit:
                files_flagged_count += 1
                print(f'OVER SIZE LIMIT, SIZE: {size}, PATH: {file}')
            # else:
            #     print(f"file under size: {file} {size}")
            #     print(f"{os_size} and {self.file_size_limit}")

        print("")
        print(f'Files found: {len(self.files)}')
        print(f'Number of size violations: {files_flagged_count}')
        print("")
        
        print("The following files returned a size of zero. Please manually verify the following files as a size of zero is probably not correct.")
        print("Note that some of these might be folders which you can ignore.\n")
        for file in self.failed_files:
            print(file)

        print("\n")


def main():
    scanner = FileSizeScanner()

    print("Beginning scan..")
    scanner.scan_files()


if __name__ == "__main__":
    main()