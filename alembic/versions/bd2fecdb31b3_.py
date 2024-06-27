"""empty message

Revision ID: bd2fecdb31b3
Revises: 374adcb85f4a
Create Date: 2024-06-27 16:42:42.991817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd2fecdb31b3'
down_revision: Union[str, None] = '374adcb85f4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
