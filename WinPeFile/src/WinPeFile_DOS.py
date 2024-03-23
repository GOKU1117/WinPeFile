import struct

def read_dos_header(file_path):
    dos_header_format = '<60sH2IH3H'
    dos_header_size = struct.calcsize(dos_header_format)
   
    with open(file_path, 'rb') as file:
        dos_header_data = file.read(dos_header_size)
        if len(dos_header_data) != dos_header_size:
            print("Error: Unable to read DOS header")
            return None

        dos_header = struct.unpack(dos_header_format, dos_header_data)

        # Extracting relevant information from DOS header
        e_magic = dos_header[0][:2]     # Magic number
        e_lfanew = dos_header[4]        # File address of new exe header

        return e_magic, e_lfanew

def main():
    file_path = 'LineLauncher.exe'
    dos_header_info = read_dos_header(file_path)
    if dos_header_info:
        e_magic, e_lfanew = dos_header_info
        print("Magic number (e_magic):", e_magic)
        print("File address of new exe header (e_lfanew):", e_lfanew)

if __name__ == "__main__":
    main()
