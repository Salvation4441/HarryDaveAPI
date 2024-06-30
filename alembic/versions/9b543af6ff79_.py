"""empty message

Revision ID: 9b543af6ff79
Revises: 8e8391f40ea4
Create Date: 2024-06-28 14:57:39.353341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b543af6ff79'
down_revision: Union[str, None] = '8e8391f40ea4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
