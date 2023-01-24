from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
    """ reader파일 내 헤더를 스킵하고 데이터 첫 진짜 데이터를 반황한다"""
    line = reader.readline()
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    return line

def process_file(reader : TextIO) -> None:
    """실제 데이터들 출력"""
    line = skip_header(reader).strip()
    print(line)

    for line in reader:
        line = line.strip()
        print(line)




