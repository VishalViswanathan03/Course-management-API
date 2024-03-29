"""New Migration

Revision ID: 943d1792f9cd
Revises: 1c2d3b39b5d4
Create Date: 2024-03-10 07:59:34.131248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '943d1792f9cd'
down_revision: Union[str, None] = '1c2d3b39b5d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'courses', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'course_id')
    # ### end Alembic commands ###
