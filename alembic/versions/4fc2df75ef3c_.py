"""empty message

Revision ID: 4fc2df75ef3c
Revises: 4a3c8098bbc1
Create Date: 2024-06-28 14:31:58.739516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fc2df75ef3c'
down_revision: Union[str, None] = '4a3c8098bbc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
