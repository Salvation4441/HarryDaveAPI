"""empty message

Revision ID: 3652d85270cd
Revises: 337be746e026
Create Date: 2024-07-03 15:07:51.181798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3652d85270cd'
down_revision: Union[str, None] = '337be746e026'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
