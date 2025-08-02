import sqlalchemy as sa
from datetime import datetime
from src.database import metadata

accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column(
        "account_number", sa.String(length=20), nullable=False, unique=True, index=True
    ),
    sa.Column("balance", sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column("owner_name", sa.String(length=150), nullable=False, index=True),
    sa.Column("is_active", sa.Boolean, nullable=False, default=True, index=True),
    sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
    sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
)
