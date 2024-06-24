"""empty message

Revision ID: 61cdab520399
Revises: 65a33ec8b1bd
Create Date: 2024-06-13 21:47:00.594329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61cdab520399'
down_revision: Union[str, None] = '65a33ec8b1bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
