"""empty message

Revision ID: b42244d9a4c5
Revises: 1e211da8027d
Create Date: 2024-06-28 13:58:32.184806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b42244d9a4c5'
down_revision: Union[str, None] = '1e211da8027d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
