from pydantic import BaseModel,Field,computed_field

class BookingModel(BaseModel):
    user_id:int
    room_id:int
    nights:int= Field(...,ge=1)
    rates_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rates_per_night