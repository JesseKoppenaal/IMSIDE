# =============================================================================
# load here the forcing
# for now: only Q
# =============================================================================


def forc_try1():
    #subtidal
    Q = 200
    soc = 35
    sri = 0.
    
    #tidal, multiple components
    tid_comp = ['M2']
    tid_per  = [44700]
    a_tide   = [1.]
    p_tide   = [0]
        
    return (Q, soc, sri) , (tid_comp, tid_per, a_tide, p_tide)

def forc_GUA1():
    #subtidal
    Q = 15
    soc = 35
    sri = 0.5
    
    #tidal, multiple components
    #'''
    tid_comp = ['M2']
    tid_per = [44700]
    a_tide  = [0.95]
    p_tide  = [53]
    '''
    tid_comp = ['M2','M4']
    tid_per = [44700,22350]
    a_tide  = [0.95,0.1]
    p_tide  = [53,80]
    #'''
    return (Q, soc, sri) , (tid_comp, tid_per, a_tide, p_tide)


def forc_LOI1():
    #subtidal
    Q = 700
    soc = 35
    sri = 0.15
    #tidal 
    tid_comp = ['M2']
    tid_per = [44700]
    a_tide  = [1.8] #1.85
    p_tide  = [195]  #190
    
    return (Q, soc, sri) , (tid_comp, tid_per, a_tide, p_tide)

def forc_DLW1():
    #subtidal
    Q = 330
    soc = 35
    sri = 0.15
    #tidal 
    tid_comp = ['M2']
    tid_per = [44700]
    a_tide  = [0.68] #1.85
    p_tide  = [0]  #190
    
    return (Q, soc, sri) , (tid_comp, tid_per, a_tide, p_tide)

def forc_GUA1Q(Q=15):
    #subtidal
    #Q = 15
    soc = 35
    sri = 0.5
    
    #tidal, multiple components
    #'''
    tid_comp = ['M2']
    tid_per = [44700]
    a_tide  = [0.95]
    p_tide  = [53]
    '''
    tid_comp = ['M2','M4']
    tid_per = [44700,22350]
    a_tide  = [0.95,0.1]
    p_tide  = [53,80]
    #'''
    return (Q, soc, sri) , (tid_comp, tid_per, a_tide, p_tide)
