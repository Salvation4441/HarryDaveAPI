"""empty message

Revision ID: 5748af6d6967
Revises: 1c8b50710968
Create Date: 2024-06-24 14:39:58.313396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5748af6d6967'
down_revision: Union[str, None] = '1c8b50710968'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
