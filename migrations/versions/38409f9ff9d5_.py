"""empty message

Revision ID: 38409f9ff9d5
Revises: 675855158a90
Create Date: 2019-06-23 15:55:00.611881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38409f9ff9d5'
down_revision = '675855158a90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('merchant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('merchant')
    # ### end Alembic commands ###