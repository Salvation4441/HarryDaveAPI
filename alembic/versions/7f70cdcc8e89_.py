"""empty message

Revision ID: 7f70cdcc8e89
Revises: 96c096d6aa13
Create Date: 2024-06-24 12:53:38.502509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f70cdcc8e89'
down_revision: Union[str, None] = '96c096d6aa13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
