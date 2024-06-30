"""empty message

Revision ID: b0cd7f8ee904
Revises: b563080cabbd
Create Date: 2024-06-28 13:15:01.021298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0cd7f8ee904'
down_revision: Union[str, None] = 'b563080cabbd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
