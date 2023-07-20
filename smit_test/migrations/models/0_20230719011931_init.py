from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cargotypes" (
    "title" VARCHAR(255) NOT NULL  PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "tariffs" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "date" DATE NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "cargo_type_id" VARCHAR(255) NOT NULL REFERENCES "cargotypes" ("title") ON DELETE CASCADE,
    CONSTRAINT "uid_tariffs_date_cd05b3" UNIQUE ("date", "cargo_type_id")
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
