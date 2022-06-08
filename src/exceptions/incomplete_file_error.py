class IncompleteFileError(Exception):
    # Exception raises when the file is not complete
    def __init__(self, file_path: str) -> None:
        self.filename = file_path
        super().__init__(f"¡Error: el archivo '{file_path}' tiene columnas invalidas!")