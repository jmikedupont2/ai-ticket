# ai_ticket.events.inference

import ai_ticket.backends.pygithub

def get_existing_ticket(event):
    return get_backend().get_existing_ticket(event)

def get_backend():
    return ai_ticket.backends.pygithub

def create_new_ticket(event):
    return get_backend().create_new_ticket(event)

def on_event(event):

     existing_ticket = get_existing_ticket(event)
     
     if existing_ticket:
         # An existing ticket was found, return it
         return existing_ticket
     else:
         # No existing ticket found, create a new one
         new_ticket = create_new_ticket(event)
         return new_ticket
