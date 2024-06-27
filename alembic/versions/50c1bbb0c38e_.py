"""empty message

Revision ID: 50c1bbb0c38e
Revises: 4173705d79f1
Create Date: 2024-06-26 12:46:58.898086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50c1bbb0c38e'
down_revision: Union[str, None] = '4173705d79f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
