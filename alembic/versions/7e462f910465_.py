"""empty message

Revision ID: 7e462f910465
Revises: bd2fecdb31b3
Create Date: 2024-06-28 13:03:39.306400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e462f910465'
down_revision: Union[str, None] = 'bd2fecdb31b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
