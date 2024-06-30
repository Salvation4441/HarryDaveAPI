"""empty message

Revision ID: 9db18739c439
Revises: 7e462f910465
Create Date: 2024-06-28 13:09:57.891328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9db18739c439'
down_revision: Union[str, None] = '7e462f910465'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
