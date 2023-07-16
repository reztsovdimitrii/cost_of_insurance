from pydantic import BaseModel, Field, RootModel


class RateItem(BaseModel):
    cargo_type: str
    rate: str


class TariffFile(RootModel):
    root: dict[str, list[RateItem]] = Field(..., example={
        "2020-06-01": [
            {"cargo_type": "Glass", "rate": "0.04"},
            {"cargo_type": "Other", "rate": "0.01"}
        ],
        "2020-07-01": [
            {"cargo_type": "Glass", "rate": "0.035"},
            {"cargo_type": "Other", "rate": "0.015"}
        ]
    })


class CostInsurance(BaseModel):
    date: str = Field(..., example="2020-06-01")
    cargo_type: str = Field(..., example="Glass")
    declared_value: float = Field(..., example=10000)
