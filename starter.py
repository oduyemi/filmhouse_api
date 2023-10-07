import os
from filmhouse_app import run, engine, Base
from dotenv import load_dotenv
from instance.config import SECRET_KEY, DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect


load_dotenv()

os.environ["SECRET_KEY"] = os.getenv("SECRET_KEY", SECRET_KEY)
os.environ["DATABASE_URI"] = os.getenv("DATABASE_URI", DATABASE_URI)

print("Database URI:", DATABASE_URI)

Base.metadata.create_all(bind = engine)

print("Tables created")

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

with Session() as session:
    inspector = inspect(engine)
    existing_tables = Base.metadata.tables.keys()
    print("Existing tables:", existing_tables)
    session.commit()
print("Server running on port 8000")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("filmhouse_app.run:run", host="0.0.0.0", port=8000, reload=True)