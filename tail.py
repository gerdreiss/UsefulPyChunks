def tail(path, window=20):
    with open(path, 'r') as f:
        BUFSIZ = 1024
        f.seek(0, 2)
        num_bytes = f.tell()
        size = window + 1
        block = -1
        data = []
        while size > 0 and num_bytes > 0:
            if num_bytes - BUFSIZ > 0:
                # Seek back one whole BUFSIZ
                f.seek(block * BUFSIZ, 2)
                # Read BUFFER
                data.insert(0, f.read(BUFSIZ))
            else:
                # File too small, start from beginning
                f.seek(0,0)
                # Only read what was not read
                data.insert(0, f.read(num_bytes))
            linesFound = data[0].count('\n')
            size -= linesFound
            num_bytes -= BUFSIZ
            block -= 1
        return '\n'.join(''.join(data).splitlines()[-window:])