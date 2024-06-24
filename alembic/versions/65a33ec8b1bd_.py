"""empty message

Revision ID: 65a33ec8b1bd
Revises: 62769a609cd4
Create Date: 2024-06-13 12:18:12.003695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65a33ec8b1bd'
down_revision: Union[str, None] = '62769a609cd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
