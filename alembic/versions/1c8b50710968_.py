"""empty message

Revision ID: 1c8b50710968
Revises: f74a59bd1809
Create Date: 2024-06-24 14:39:55.663464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c8b50710968'
down_revision: Union[str, None] = 'f74a59bd1809'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
