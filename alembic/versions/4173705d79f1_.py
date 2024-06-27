"""empty message

Revision ID: 4173705d79f1
Revises: 34eb8ac00994
Create Date: 2024-06-26 12:06:35.923174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4173705d79f1'
down_revision: Union[str, None] = '34eb8ac00994'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
