"""empty message

Revision ID: c8c9b7195a03
Revises: c5dad0239679
Create Date: 2024-06-28 14:06:40.935345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8c9b7195a03'
down_revision: Union[str, None] = 'c5dad0239679'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
