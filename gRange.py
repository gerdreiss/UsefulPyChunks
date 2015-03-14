def gRange(s,e,step=1):
  ''' generalized range
      create ranges of any object type
      s and e need to be comparable by <
      s and step need to produce an s when subjected to s+step

      good for dates, for example:
      gRange(datetime.date(2015,1,1),
             datetime.date(2015,1,10),
             datetime.timedelta(days=1))
  '''
  ret = []
  while s<e:
    ret.append(s)
    s = s+step
  return ret

def gRangeGen(s,e,step=1):
    ''' generalized range
        create ranges of any object type
        s and e need to be comparable by <
        s and step need to produce an s when subjected to s+step

        good for dates, for example:
        gRange(datetime.date(2015,1,1),
               datetime.date(2015,1,10),
               datetime.timedelta(days=1))
    '''
    while s < e:
        yield s
        s = s + step