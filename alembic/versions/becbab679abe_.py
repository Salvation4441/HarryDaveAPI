"""empty message

Revision ID: becbab679abe
Revises: a2c10742dc04
Create Date: 2024-07-08 12:52:46.262887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'becbab679abe'
down_revision: Union[str, None] = 'a2c10742dc04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
