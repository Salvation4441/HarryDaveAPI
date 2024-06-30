"""empty message

Revision ID: c6f26276e8cb
Revises: b42244d9a4c5
Create Date: 2024-06-28 14:00:27.166802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6f26276e8cb'
down_revision: Union[str, None] = 'b42244d9a4c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
