"""empty message

Revision ID: 3d73a572a083
Revises: c8c9b7195a03
Create Date: 2024-06-28 14:07:26.577373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d73a572a083'
down_revision: Union[str, None] = 'c8c9b7195a03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
