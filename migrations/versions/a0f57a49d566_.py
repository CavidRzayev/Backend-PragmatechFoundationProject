"""empty message

Revision ID: a0f57a49d566
Revises: 27ffd3f52fab
Create Date: 2021-02-08 11:03:25.069459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0f57a49d566'
down_revision = '27ffd3f52fab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###