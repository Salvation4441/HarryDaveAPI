"""empty message

Revision ID: 374adcb85f4a
Revises: 50c1bbb0c38e
Create Date: 2024-06-27 15:21:14.655200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '374adcb85f4a'
down_revision: Union[str, None] = '50c1bbb0c38e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
