
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

class TicketInput(BaseModel):
    tickets: list

@app.post("/summarize")
def summarize_tickets(input_data: TicketInput):

    prompt = f"""
    You are a product manager assistant.

    Summarize the following customer support tickets into:
    - Issue
    - Impact
    - Urgency

    Rules:
    - Be concise
    - No assumptions
    - No extra commentary

    Tickets:
    {input_data.tickets}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=250,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "summary": response.choices[0].message.content
    }
