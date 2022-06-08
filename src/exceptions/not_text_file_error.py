class NotTextFileError(Exception):
    # Exception raises when the file is not a text file
    def __init__(self, file_path: str) -> None:
        self.filename = file_path
        super().__init__(f"¡Error: el archivo '{file_path}' no es un archivo de texto!")