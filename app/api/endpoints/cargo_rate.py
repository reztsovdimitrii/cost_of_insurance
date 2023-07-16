from fastapi import APIRouter, File, HTTPException, UploadFile
from tortoise.exceptions import DoesNotExist

from app.models.cargo_rate import CargoRate
from app.schemas.cargo_rate import CostInsurance, RateItem, TariffFile

from .utils import save_tatiff_data

router = APIRouter()


@router.get("/all_tariff", response_model=TariffFile)
async def get_current_tariff_all_date():
    try:
        objs = await CargoRate.all()
        formatted_tariff = {}
        for obj in objs:
            date = obj.date.strftime("%Y-%m-%d")
            cargo_type = obj.cargo_type
            rate = str(obj.rate)
            if date not in formatted_tariff:
                formatted_tariff[date] = []
            formatted_tariff[date].append(
                RateItem(
                    cargo_type=cargo_type,
                    rate=rate))
        return formatted_tariff
    except DoesNotExist:
        return {"error": "No tariff found"}


@router.post("/upload_tariff_file")
async def upload_tariff_file(
    tariff_file: UploadFile = File(...)
):
    if tariff_file is None:
        raise HTTPException(status_code=400, detail="No tariff file provided")

    if tariff_file:
        try:
            tariff_data = await tariff_file.read()
            tariff_data = TariffFile.model_validate_json(tariff_data)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid tariff file")

    return await save_tatiff_data(tariff_data)


@router.post("/upload_tariff_data")
async def upload_tariff_date(
    tariff_data: TariffFile
):
    if tariff_data is None:
        raise HTTPException(status_code=400, detail="No tariff data provided")

    return await save_tatiff_data(tariff_data)


@router.post("/get_cost_of_insurance")
async def get_cost_of_insurance(data: CostInsurance):
    try:
        obj = await CargoRate.filter(
            date=data.date,
            cargo_type=data.cargo_type).get()
        cost_insurance = data.declared_value * obj.rate
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Rate not found")
    return {"cost_insurance": str(cost_insurance)}
