"""empty message

Revision ID: 72226c4819b7
Revises: 338bb8027cb9
Create Date: 2020-09-17 17:25:35.637454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72226c4819b7'
down_revision = '338bb8027cb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###