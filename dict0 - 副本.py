    import collections  
      
    print 'Regular dictionary:'  
    d1={}  
    d1['a']='A'  
    d1['b']='B'  
    d1['c']='C'  
      
    d2={}  
    d2['c']='C'  
    d2['a']='A'  
    d2['b']='B'  
      
    print d1==d2  
      
    print '\nOrderedDict:'  
    d1=collections.OrderedDict()  
    d1['a']='A'  
    d1['b']='B'  
    d1['c']='C'  
      
    d2=collections.OrderedDict()  
    d2['c']='C'  
    d2['a']='A'  
    d2['b']='B'  
      
    print  d1==d2  

dd = {'banana':3,'apple':4,'pear':1,'orange':2}
print dd
print sorted(dd.items())