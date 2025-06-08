"""
Решение задачи на релаизацию обработчика файлов различных типов (наивный подход)
"""


class FileHandler:
    def read_csv(self, path: str) -> list[str]:
        return ["a", "b", "c"]

    def read_excel(self, path: str) -> list[str]:
        return ["a", "b", "c", "d"]

    def process(self, path: str) -> int:
        file_type = path.split(".")[-1]
        if file_type == "csv":
            content = self.read_csv(path)
        elif file_type == "xlsx":
            content = self.read_excel(path)
        else:
            raise ValueError(f"File type is not implemented: {file_type}")

        print("Rows:", len(content))
        return len(content)


def client_code():
    reader = FileHandler()
    reader.process("file.csv")
    reader.process("file.xlsx")


if __name__ == "__main__":
    client_code()
