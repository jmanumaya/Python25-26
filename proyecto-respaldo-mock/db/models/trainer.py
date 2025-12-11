from typing import Optional
from pydantic import BaseModel

# Entidad Trainer
class Trainer(BaseModel):
    id: Optional[str] = None
    name: str
    specialty: str  # Crossfit, Yoga, Musculación, etc.
    shift: str  # Mañana, Tarde