"""empty message

Revision ID: c5dad0239679
Revises: a6f965665c38
Create Date: 2024-06-28 14:06:06.713996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5dad0239679'
down_revision: Union[str, None] = 'a6f965665c38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
