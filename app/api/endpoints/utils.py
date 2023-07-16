from fastapi import HTTPException

from app.models.cargo_rate import CargoRate


async def save_tatiff_data(tariff_data):
    try:
        for date, rates in tariff_data.root.items():
            for rate_item in rates:
                cargo_rate = CargoRate(
                    date=date,
                    cargo_type=rate_item.cargo_type,
                    rate=float(rate_item.rate)
                )
                await cargo_rate.save()

        return {"message": "Tariff uploaded successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to upload tariff: {e}"
        )
