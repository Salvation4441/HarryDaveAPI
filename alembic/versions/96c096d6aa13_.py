"""empty message

Revision ID: 96c096d6aa13
Revises: 19f6cdc4901d
Create Date: 2024-06-24 12:50:04.004430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96c096d6aa13'
down_revision: Union[str, None] = '19f6cdc4901d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
