"""empty message

Revision ID: b563080cabbd
Revises: 9db18739c439
Create Date: 2024-06-28 13:14:57.211666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b563080cabbd'
down_revision: Union[str, None] = '9db18739c439'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
