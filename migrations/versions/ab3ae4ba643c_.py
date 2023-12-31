"""empty message

Revision ID: ab3ae4ba643c
Revises: 
Create Date: 2023-08-08 14:28:58.926101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3ae4ba643c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=700), nullable=True),
    sa.Column('short_url', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('url_data', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_url_data_short_url'), ['short_url'], unique=True)
        batch_op.create_index(batch_op.f('ix_url_data_url'), ['url'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url_data', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_url_data_url'))
        batch_op.drop_index(batch_op.f('ix_url_data_short_url'))

    op.drop_table('url_data')
    # ### end Alembic commands ###
