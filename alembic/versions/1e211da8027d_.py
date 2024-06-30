"""empty message

Revision ID: 1e211da8027d
Revises: b0cd7f8ee904
Create Date: 2024-06-28 13:50:33.039229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e211da8027d'
down_revision: Union[str, None] = 'b0cd7f8ee904'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
