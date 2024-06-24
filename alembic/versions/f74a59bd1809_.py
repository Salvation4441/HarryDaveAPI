"""empty message

Revision ID: f74a59bd1809
Revises: 7f70cdcc8e89
Create Date: 2024-06-24 14:12:26.074261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f74a59bd1809'
down_revision: Union[str, None] = '7f70cdcc8e89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
