"""add users table

Revision ID: d8a9b94b447f
Revises: b395c61af56e
Create Date: 2021-12-08 17:21:42.583457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8a9b94b447f'
down_revision = 'b395c61af56e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
