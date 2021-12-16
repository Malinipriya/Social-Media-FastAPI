"""add content column

Revision ID: b395c61af56e
Revises: 56e8e9cfbc14
Create Date: 2021-12-08 17:14:16.923075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b395c61af56e'
down_revision = '56e8e9cfbc14'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass