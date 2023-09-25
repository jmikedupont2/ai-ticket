# ai_ticket.events.inference

import ai_ticket.backends.pygithub

def get_existing_ticket(event):
    return get_backend().get_existing_ticket(event)

def get_backend():
    return ai_ticket.backends.pygithub

def create_new_ticket(event):
    return get_backend().create_new_ticket(event)

def create_new_comment(ticket, event):
    return get_backend().create_new_comment(ticket, event)

def on_event(event):
    #print(event)
    
    ticket = get_existing_ticket(event)
     
    if not ticket:
         # No existing ticket found, create a new one
         ticket = create_new_ticket(event)

    return create_new_comment(ticket, event )
    
