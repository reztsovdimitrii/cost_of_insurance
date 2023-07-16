from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cargo_rates" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(255) NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "date" DATE NOT NULL,
    CONSTRAINT "uid_cargo_rates_date_64f77e" UNIQUE ("date", "cargo_type")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
