"""empty message

Revision ID: 86b388ed4e53
Revises: 6d1a30c4f30f
Create Date: 2021-02-08 11:55:29.308166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86b388ed4e53'
down_revision = '6d1a30c4f30f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name1', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer', schema=None) as batch_op:
        batch_op.drop_column('name1')

    # ### end Alembic commands ###
