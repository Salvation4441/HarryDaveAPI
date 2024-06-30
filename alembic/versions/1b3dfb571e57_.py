"""empty message

Revision ID: 1b3dfb571e57
Revises: c6f26276e8cb
Create Date: 2024-06-28 14:01:49.331603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b3dfb571e57'
down_revision: Union[str, None] = 'c6f26276e8cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
