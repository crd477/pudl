"""Add utility type

Revision ID: ad3e7ecdcfc3
Revises: 13b9fb61c466
Create Date: 2023-09-27 15:06:27.671649

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ad3e7ecdcfc3'
down_revision = '13b9fb61c466'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('balance_sheet_assets_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('denorm_balance_sheet_assets_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('denorm_plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('plant_status', sa.Text(), nullable=True, comment='Utility plant financial status (in service, future, leased, total).'))

    with op.batch_alter_table('plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('plant_status', sa.Text(), nullable=True, comment='Utility plant financial status (in service, future, leased, total).'))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.drop_column('plant_status')

    with op.batch_alter_table('denorm_plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.drop_column('plant_status')

    with op.batch_alter_table('denorm_balance_sheet_assets_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('balance_sheet_assets_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    # ### end Alembic commands ###
