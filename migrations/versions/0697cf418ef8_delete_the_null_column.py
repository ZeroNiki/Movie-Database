"""Delete the null column

Revision ID: 0697cf418ef8
Revises: ce03316f64a1
Create Date: 2024-09-02 12:42:29.591581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0697cf418ef8'
down_revision: Union[str, None] = 'ce03316f64a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'backdrop_path')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('backdrop_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
