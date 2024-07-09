"""empty message

Revision ID: 337be746e026
Revises: 2c7e2245b601
Create Date: 2024-07-02 14:28:44.790901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '337be746e026'
down_revision: Union[str, None] = '2c7e2245b601'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
