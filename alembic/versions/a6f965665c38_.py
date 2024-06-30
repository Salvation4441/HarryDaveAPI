"""empty message

Revision ID: a6f965665c38
Revises: 39e91ced5fd0
Create Date: 2024-06-28 14:05:05.350303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6f965665c38'
down_revision: Union[str, None] = '39e91ced5fd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
