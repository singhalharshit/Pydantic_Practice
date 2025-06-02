from pydantic import BaseModel
from typing import List, Optional

# This is a simple model to hold address-related fields
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


# Nested Model Example:
# Here, we're using Address inside the User model.
# This is called "nested model referencing" — it allows us to structure related data clearly.
class User(BaseModel):
    id: int
    name: str
    address: Address  # ✅ Nested Pydantic model. It expects an Address object here.


# Self-Referencing Model Example:
# Sometimes a model needs to refer to itself — like a comment that has replies (which are also comments).
# In such cases, we use forward references by passing the class name as a string: 'Comment'.
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # ✅ Self-referencing using forward declaration

# Pydantic needs to rebuild the model after forward references.
# This step tells Pydantic to resolve the forward references properly.
Comment.model_rebuild()


# Creating objects with nested models
address = Address(street="123 something", city="Jaipur", postal_code="10001")
user = User(id=1, name="Harshit", address=address)

# Creating a recursive comment structure
comment = Comment(
    id=1,
    content="something something",
    replies=[Comment(id=2, content="second value")]
)
