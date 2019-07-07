"""add created updated columns to merchant table

Revision ID: 06170fcc6c51
Revises: 38409f9ff9d5
Create Date: 2019-06-23 16:15:47.446574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06170fcc6c51'
down_revision = '38409f9ff9d5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('merchant', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('merchant', sa.Column('updated', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('merchant', 'created')
    op.drop_column('merchant', 'updated')
