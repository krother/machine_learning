
Project: AI Pizza Delivery Service
==================================

Goal
----

The goal of this project is to develop an AI-powered agent for a pizza delivery service. The agent manages a dialog with a customer. It asks what pizzas and extra toppings from a defined catalog the customer wants to order. Special requests such as allergies or vegan / halal should be answered. The agent needs to record a delivery address as well. In the end, the agent produces an order in a structured format.

Requirements
------------

- the project is done in a team of 2-4 people
- there is a defined menu of pizzas/optional toppings/extras
- there is a defined flowchart for the dialog
- a prompt for the local model is implemented
- the recorded order is produced in a structured data format (JSON, CSV, XML, SQL)
- there is a screenshot / transcript / recording of the working agent
- there is a PDF report of 2 pages max.
- there is a program that runs the agent
- the project is made available on GitHub
- there is a user interface (web app or mobile interface)
- the agent can process spoken language
- the agent can answer in spoken language
- other creative additions of your own choice

Implementation
--------------

The project implementation should include at least one language model (local SLM or LLM via an API). It may include other models to satisfy the extra requirements below. To pass the course, a single model with a handcrafted prompt is sufficient.

To guide the dialog, a flowchart should be created that explains the dialog and decisions made by the agent. For creating flowcharts, I recommend https://mermaid.live .

Ideally, the agent not only records the order but also asks the user for extra information, e.g. "lots of onions", "spicy" or "very spicy". If any information is missing, the agent comes back and asks extra questions to complete all essential fields.

For a good grade, there should be a program that connects the pieces.
For an excellent grade, the program/model is available through a user interface using spoken language, work through a web application, mobile app or similar. Extra points will be awarded for creative solutions.

Part of the project is a report that describes the implementation, the technologies and prompts used and the flowchart. The report should also provide evidence that the dialog is working and reflect on any known issues.

.. hint::

   If you don't like pizza, or have some other great idea, use a restaurant type of your choice instead.
