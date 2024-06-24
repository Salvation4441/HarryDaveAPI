"""empty message

Revision ID: 19f6cdc4901d
Revises: 61cdab520399
Create Date: 2024-06-24 12:47:33.609918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f6cdc4901d'
down_revision: Union[str, None] = '61cdab520399'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
