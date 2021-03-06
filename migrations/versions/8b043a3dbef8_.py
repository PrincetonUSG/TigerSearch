"""empty message

Revision ID: 8b043a3dbef8
Revises: 525d497d87b4
Create Date: 2021-12-04 23:25:57.579009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b043a3dbef8'
down_revision = '525d497d87b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isAdmin', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('users', sa.Column('isBanned', sa.Boolean(), server_default='false', nullable=False))
    op.drop_column('users', 'banned')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('banned', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'isBanned')
    op.drop_column('users', 'isAdmin')
    # ### end Alembic commands ###
