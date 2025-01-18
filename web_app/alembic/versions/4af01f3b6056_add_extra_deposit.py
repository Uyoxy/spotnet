"""Add extra deposit

Revision ID: 4af01f3b6056
Revises: 4987a0457799
Create Date: 2025-01-17 18:15:08.467337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4af01f3b6056'
down_revision = '4987a0457799'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extra_deposits',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('token_symbol', sa.String(), nullable=False),
    sa.Column('amount', sa.String(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.Column('position_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['position_id'], ['position.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token_symbol')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('extra_deposits')
    # ### end Alembic commands ###
