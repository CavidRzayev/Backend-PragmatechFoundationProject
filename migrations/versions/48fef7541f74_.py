"""empty message

Revision ID: 48fef7541f74
Revises: d20cfb2935e2
Create Date: 2021-02-08 11:13:04.971022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48fef7541f74'
down_revision = 'd20cfb2935e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('adress', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer', schema=None) as batch_op:
        batch_op.drop_column('adress')

    # ### end Alembic commands ###