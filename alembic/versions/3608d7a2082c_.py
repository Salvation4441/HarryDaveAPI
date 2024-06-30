"""empty message

Revision ID: 3608d7a2082c
Revises: 9b543af6ff79
Create Date: 2024-06-28 15:36:03.843125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3608d7a2082c'
down_revision: Union[str, None] = '9b543af6ff79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
