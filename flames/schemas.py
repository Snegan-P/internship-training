from pydantic import BaseModel

class FlamesRequest(BaseModel):
    name1: str
    name2: str