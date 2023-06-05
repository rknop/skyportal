"""Instrument log migration

Revision ID: 13b080112d9c
Revises: e2273768afa4
Create Date: 2023-06-05 11:07:38.545038

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '13b080112d9c'
down_revision = 'e2273768afa4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'instrumentlogs',
        sa.Column('instrument_id', sa.Integer(), nullable=False),
        sa.Column('start_date', sa.DateTime(), nullable=False),
        sa.Column('end_date', sa.DateTime(), nullable=False),
        sa.Column('log', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('modified', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ['instrument_id'], ['instruments.id'], ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(
        op.f('ix_instrumentlogs_created_at'),
        'instrumentlogs',
        ['created_at'],
        unique=False,
    )
    op.create_index(
        op.f('ix_instrumentlogs_end_date'), 'instrumentlogs', ['end_date'], unique=False
    )
    op.create_index(
        op.f('ix_instrumentlogs_start_date'),
        'instrumentlogs',
        ['start_date'],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_instrumentlogs_start_date'), table_name='instrumentlogs')
    op.drop_index(op.f('ix_instrumentlogs_end_date'), table_name='instrumentlogs')
    op.drop_index(op.f('ix_instrumentlogs_created_at'), table_name='instrumentlogs')
    op.drop_table('instrumentlogs')
    # ### end Alembic commands ###
