"""empty message

Revision ID: 8e8391f40ea4
Revises: 8e581294d57c
Create Date: 2024-06-28 14:40:43.819083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e8391f40ea4'
down_revision: Union[str, None] = '8e581294d57c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
