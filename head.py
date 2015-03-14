def head(path, lines=20):
    with open(path, 'r') as handle:
        return ''.join(handle.next() for line in xrange(lines))