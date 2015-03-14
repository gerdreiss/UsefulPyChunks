import datetime
import os.path

def time_stamp(filename):
    ''' injects a timestamp into a file name '''

    name, ext = os.path.splitext(filename)
    timestamp =  '_'.join([str(x) for x in datetime.datetime.now().timetuple()[:6]])

    return '{0}__{1}{2}'.format(name, timestamp, ext)