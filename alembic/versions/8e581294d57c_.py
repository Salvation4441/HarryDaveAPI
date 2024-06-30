"""empty message

Revision ID: 8e581294d57c
Revises: 4fc2df75ef3c
Create Date: 2024-06-28 14:35:20.234123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e581294d57c'
down_revision: Union[str, None] = '4fc2df75ef3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
