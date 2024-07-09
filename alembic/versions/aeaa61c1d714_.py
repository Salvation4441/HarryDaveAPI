"""empty message

Revision ID: aeaa61c1d714
Revises: 3608d7a2082c
Create Date: 2024-07-02 13:04:08.371177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aeaa61c1d714'
down_revision: Union[str, None] = '3608d7a2082c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
