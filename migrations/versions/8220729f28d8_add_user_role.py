"""Add user Role

Revision ID: 8220729f28d8
Revises: 8467ee03c194
Create Date: 2026-08-20 23:37:05.643089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8220729f28d8'
down_revision = '8467ee03c194'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'role',
                sa.String(length=20),
                nullable=False,
                server_default='user'
            )
        )

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
