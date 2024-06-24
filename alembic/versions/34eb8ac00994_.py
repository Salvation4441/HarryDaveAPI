"""empty message

Revision ID: 34eb8ac00994
Revises: 5748af6d6967
Create Date: 2024-06-24 14:40:04.014209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34eb8ac00994'
down_revision: Union[str, None] = '5748af6d6967'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
