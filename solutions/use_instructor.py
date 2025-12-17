"""
pip install instructor pydantic
"""
import instructor
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    occupation: str

    model_config = {
        "populate_by_name": True,
        "strict": False  # erlaubt Konvertierungen
    }

# Works with any provider - same interface everywhere
# client = instructor.from_provider("openai/gpt-5-nano")
# client = instructor.from_provider("anthropic/claude-3")
# client = instructor.from_provider("google/gemini-pro")
client = instructor.from_provider("ollama/gemma3:1b")  # local

# Extract structured data from natural language
person = client.create(
    response_model=Person,
    messages=[
        {"role": "user", "content": "Extract: Ada is a 30-year-old software engineer"}
    ],
)
print(person)
print(person.name)
print(person.age)
