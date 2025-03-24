"""Create MMT instrument API for followup

Revision ID: 7eab209f29d3
Revises: 4e85d7afc22c
Create Date: 2025-03-23 21:04:42.349448

"""

import sqlalchemy as sa
import sqlalchemy_utils

from alembic import op

# revision identifiers, used by Alembic.
revision = "7eab209f29d3"
down_revision = "4e85d7afc22c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE followup_apis ADD VALUE IF NOT EXISTS 'BINOSPECAPI'")
        op.execute("ALTER TYPE followup_apis ADD VALUE IF NOT EXISTS 'MMIRSAPI'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
