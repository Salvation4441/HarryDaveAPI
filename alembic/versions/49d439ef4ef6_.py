"""empty message

Revision ID: 49d439ef4ef6
Revises: 3d73a572a083
Create Date: 2024-06-28 14:08:02.022518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49d439ef4ef6'
down_revision: Union[str, None] = '3d73a572a083'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
