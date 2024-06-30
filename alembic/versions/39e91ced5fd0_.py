"""empty message

Revision ID: 39e91ced5fd0
Revises: 1b3dfb571e57
Create Date: 2024-06-28 14:03:13.944203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39e91ced5fd0'
down_revision: Union[str, None] = '1b3dfb571e57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
