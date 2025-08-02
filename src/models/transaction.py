import sqlalchemy as sa
from src.database import metadata
from datetime import datetime

transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
    sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column("published_at", sa.TIMESTAMP(), nullable=False, default=datetime.now),
    sa.Column(
        "transaction_type",
        sa.Enum("withdrawal", "deposit", name="transaction_type_enum"),
        nullable=False,
    ),
)
