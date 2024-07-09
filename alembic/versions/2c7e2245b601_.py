"""empty message

Revision ID: 2c7e2245b601
Revises: 4abecf200965
Create Date: 2024-07-02 14:24:39.328793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c7e2245b601'
down_revision: Union[str, None] = '4abecf200965'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
