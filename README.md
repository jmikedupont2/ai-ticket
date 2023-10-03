# AI-Ticket
The AI Ticket system to handle the AI with tickets.
Human Powered AI-Ops to Help you with the last mile of your AI code generated system.


**Summary: User-Driven Ticket-Based Workflow**

Welcome to our innovative user-driven workflow, designed to empower you to interact with our system like a large language model. Here's a quick overview of what we're doing:

**1. User as Language Model**:
   - You take on the role of a large language model proxy.

**2. Step-by-Step Interaction**:
   - Each interaction with the system occurs step by step.
   - At each step, you generate a query or response, which becomes a "ticket."

**3. Proxy Server**:
   - A proxy server facilitates your interactions, creating a ticket for each step.

**4. Request Assistance Action**:
   - AutoGPT integrates with this workflow using a "Request Assistance" action.
   - This action includes the URL of the GitHub ticket comment linked to your query.

**5. User-Controlled Process**:
   - You guide the workflow, making decisions, and generating tickets at each step.

**6. Ticket-Based Workflow**:
   - Each ticket records a step in your interaction, ensuring documentation and continuity.

**7. AutoGPT's Role**:
   - AutoGPT waits for ticket updates with valid responses generated by you.
   - It retriggers actions based on your responses to move the workflow forward.

**8. Potential Stalls**:
   - Be mindful of providing timely and appropriate responses to prevent workflow stalls.

This user-driven ticket-based workflow offers flexibility, control, and a unique way to collaborate with our system. Dive in, generate tickets, and explore the possibilities of this interactive and dynamic approach.


# Infrastructure

The docker images are organized like this :

* act_base is the foundation of all actions. 
* poetry_base is contains the poetry magic layer with shared containers.
