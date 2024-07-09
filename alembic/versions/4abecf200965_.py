"""empty message

Revision ID: 4abecf200965
Revises: aeaa61c1d714
Create Date: 2024-07-02 13:54:17.986153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4abecf200965'
down_revision: Union[str, None] = 'aeaa61c1d714'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
