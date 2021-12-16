"""add last few columns to posts table

Revision ID: 8b0e0519f20e
Revises: 3d7c89055c78
Create Date: 2021-12-15 14:36:06.114694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b0e0519f20e'
down_revision = '3d7c89055c78'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    pass
