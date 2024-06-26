"""empty message

Revision ID: 0a36ea941017
Revises: 5d18ee6da174
Create Date: 2024-05-04 17:53:25.549211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a36ea941017'
down_revision = '5d18ee6da174'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gastronomy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('text', sa.String(length=1000), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gastronomy')
    # ### end Alembic commands ###
