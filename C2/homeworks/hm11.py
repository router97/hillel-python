# Homework 11 - File class

import os
from shutil import rmtree
from random import randint, choice
from content import content

class File:
    """A class representing a file"""
    
    GEN_FOLDER = os.path.join(os.getcwd(), 'files')
    FILE_NAME = 'file'
    
    def __init__(self, name: str, content: str, size: int, created_at: float, path: str = None) -> None:
        self.name: str = name
        self.content: str = content
        self.size: int = size
        self.created_at: float = created_at
        self.path: str = path if path else os.path.join(self.GEN_FOLDER, self.name)
    
    def __str__(self) -> str:
        return f'{self.name}(size = {self.size} bytes, created_at = {self.created_at})'
    
    @classmethod
    def generate_files_objects(cls) -> list:
        """Generate a list of File objects from the file folder"""
        result = []
        
        for file in os.scandir(File.GEN_FOLDER):
            file_stat = file.stat()
            
            with open(file.path, 'r') as file_read:
                result.append(cls(file.name, file_read.read(), file_stat.st_size, file_stat.st_birthtime, file.path))
        
        return result
    
    @staticmethod
    def generate_files() -> None:
        """Clear the file folder and generate a random amount of files with random content in the file folder"""
        
        rmtree(File.GEN_FOLDER, ignore_errors = True)
        os.mkdir(File.GEN_FOLDER)
        
        for i in range(randint(2, 10)):
            with open(os.path.join(File.GEN_FOLDER, f"{File.FILE_NAME}_{i}.txt"), 'x') as file:
                file.write(choice(content))
    
    @staticmethod
    def list_files() -> list[str]:
        """Return and print a list of all the files in the file folder"""
        result = [file for file in os.scandir(File.GEN_FOLDER)]
        print(f'{len(result)} files: {result}')
        return result


if __name__ == '__main__':
    File.generate_files()
    file_objects = File.generate_files_objects()
    
    print('FILE INFO FROM CLASS METHOD:')
    print(f'{len(file_objects)} files:')
    for file in file_objects: 
        print(f'File(name = {file.name}, content = {file.content}, created_at = {file.created_at}, path = {file.path}, size = {file.size} )')
    
    print('\nSTATIC METHOD:')
    File.list_files()
    