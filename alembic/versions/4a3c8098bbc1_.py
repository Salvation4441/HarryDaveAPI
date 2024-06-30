"""empty message

Revision ID: 4a3c8098bbc1
Revises: 49d439ef4ef6
Create Date: 2024-06-28 14:15:08.853590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a3c8098bbc1'
down_revision: Union[str, None] = '49d439ef4ef6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
