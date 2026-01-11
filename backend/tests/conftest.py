import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.core.database import Base, get_db
from app.main import app
from tests.seeds.monthly_averages_seed import seed_monthly_averages

os.environ["ENVIRONMENT"] = "test"
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

engine = create_engine(
    "sqlite:///./test.db",
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    seed_monthly_averages(db)
    db.close()

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(db):
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
