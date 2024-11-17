def love_meet(bob, alice):
    bob_set = set(bob)
    alice_set = set(alice)
    
    path = bob_set & alice_set
    return path
    

def affair_meet(bob, alice, silvester):
    bob_set = set(bob)
    alice_set = set(alice)
    silvester_set = set(silvester)
    
    path = (silvester_set & alice_set) - bob_set
    return path