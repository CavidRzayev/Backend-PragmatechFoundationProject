"""empty message

Revision ID: 7665c31efd03
Revises: 7f86032c5cf6
Create Date: 2021-02-07 10:34:36.035354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7665c31efd03'
down_revision = '7f86032c5cf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about',
    sa.Column('about_id', sa.Integer(), nullable=False),
    sa.Column('about_text', sa.String(length=255), nullable=False),
    sa.Column('about_title', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('about_id')
    )
    op.create_table('skill',
    sa.Column('skill_id', sa.Integer(), nullable=False),
    sa.Column('percent', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('about_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['about_id'], ['about.about_id'], ),
    sa.PrimaryKeyConstraint('skill_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skill')
    op.drop_table('about')
    # ### end Alembic commands ###