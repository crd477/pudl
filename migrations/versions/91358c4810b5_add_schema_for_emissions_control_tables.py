"""Add schema for emissions control tables.

Revision ID: 91358c4810b5
Revises: 29d443aadf25
Create Date: 2023-05-16 15:39:26.766188
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "91358c4810b5"
down_revision = "29d443aadf25"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "denorm_emissions_control_equipment_eia860",
        sa.Column(
            "report_year",
            sa.Integer(),
            nullable=False,
            comment="Four-digit year in which the data was reported.",
        ),
        sa.Column(
            "plant_id_eia",
            sa.Integer(),
            nullable=False,
            comment="The unique six-digit facility identification number, also called an ORISPL, assigned by the Energy Information Administration.",
        ),
        sa.Column(
            "plant_id_pudl",
            sa.Integer(),
            nullable=True,
            comment="A manually assigned PUDL plant ID. May not be constant over time.",
        ),
        sa.Column("plant_name_eia", sa.Text(), nullable=True, comment="Plant name."),
        sa.Column(
            "utility_id_eia",
            sa.Integer(),
            nullable=True,
            comment="The EIA Utility Identification number.",
        ),
        sa.Column(
            "utility_id_pudl",
            sa.Integer(),
            nullable=True,
            comment="A manually assigned PUDL utility ID. May not be stable over time.",
        ),
        sa.Column(
            "utility_name_eia",
            sa.Text(),
            nullable=True,
            comment="The name of the utility.",
        ),
        sa.Column(
            "emission_control_id_pudl",
            sa.Float(),
            nullable=False,
            comment="A PUDL-generated ID used to distinguish emission control units in the same report year and plant id. This ID should not be used to track units over time or between plants.",
        ),
        sa.Column(
            "data_maturity",
            sa.Text(),
            nullable=True,
            comment="Level of maturity of the data record. Some data sources report less-than-final data. PUDL sometimes includes this data, but use at your own risk.",
        ),
        sa.Column(
            "emission_control_equipment_type",
            sa.Text(),
            nullable=True,
            comment="The type of emission control equipment installed.",
        ),
        sa.Column(
            "operational_status_code",
            sa.Text(),
            nullable=True,
            comment="The operating status of the asset.",
        ),
        sa.Column(
            "operational_status",
            sa.Text(),
            nullable=True,
            comment="The operating status of the asset. For generators rhis is based on which tab the generator was listed in in EIA 860.",
        ),
        sa.Column(
            "mercury_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Mercury control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "nox_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Nitrogen oxide control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "particulate_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Particulate matter control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "so2_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Sulfur dioxide control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "acid_gas_control",
            sa.Boolean(),
            nullable=True,
            comment="Indicates whether the emissions control equipment controls acid (HCl) gas.",
        ),
        sa.Column(
            "emission_control_equipment_cost",
            sa.Float(),
            nullable=True,
            comment="The total cost to install a piece of emission control equipment.",
        ),
        sa.Column(
            "emission_control_operating_date",
            sa.Date(),
            nullable=True,
            comment="The date a piece of emissions control equipment began operating. Derived from month and year columns in the raw data.",
        ),
        sa.Column(
            "emission_control_retirement_date",
            sa.Date(),
            nullable=True,
            comment="The expected or actual retirement date for a piece of emissions control equipment. Derived from month and year columns in the raw data.",
        ),
        sa.ForeignKeyConstraint(
            ["data_maturity"],
            ["data_maturities.code"],
        ),
        sa.ForeignKeyConstraint(
            ["operational_status_code"],
            ["operational_status_eia.code"],
        ),
        sa.ForeignKeyConstraint(
            ["plant_id_eia"],
            ["plants_entity_eia.plant_id_eia"],
        ),
        sa.ForeignKeyConstraint(
            ["plant_id_pudl"],
            ["plants_pudl.plant_id_pudl"],
        ),
        sa.ForeignKeyConstraint(
            ["utility_id_eia"],
            ["utilities_entity_eia.utility_id_eia"],
        ),
        sa.ForeignKeyConstraint(
            ["utility_id_pudl"],
            ["utilities_pudl.utility_id_pudl"],
        ),
        sa.PrimaryKeyConstraint(
            "report_year", "plant_id_eia", "emission_control_id_pudl"
        ),
    )
    op.create_table(
        "emissions_control_equipment_eia860",
        sa.Column(
            "report_year",
            sa.Integer(),
            nullable=False,
            comment="Four-digit year in which the data was reported.",
        ),
        sa.Column(
            "plant_id_eia",
            sa.Integer(),
            nullable=False,
            comment="The unique six-digit facility identification number, also called an ORISPL, assigned by the Energy Information Administration.",
        ),
        sa.Column(
            "emission_control_id_pudl",
            sa.Float(),
            nullable=False,
            comment="A PUDL-generated ID used to distinguish emission control units in the same report year and plant id. This ID should not be used to track units over time or between plants.",
        ),
        sa.Column(
            "data_maturity",
            sa.Text(),
            nullable=True,
            comment="Level of maturity of the data record. Some data sources report less-than-final data. PUDL sometimes includes this data, but use at your own risk.",
        ),
        sa.Column(
            "emission_control_equipment_type",
            sa.Text(),
            nullable=True,
            comment="The type of emission control equipment installed.",
        ),
        sa.Column(
            "operational_status_code",
            sa.Text(),
            nullable=True,
            comment="The operating status of the asset.",
        ),
        sa.Column(
            "mercury_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Mercury control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "nox_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Nitrogen oxide control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "particulate_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Particulate matter control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "so2_control_id_eia",
            sa.Text(),
            nullable=True,
            comment="Sulfur dioxide control identification number. This ID is not a unique identifier.",
        ),
        sa.Column(
            "acid_gas_control",
            sa.Boolean(),
            nullable=True,
            comment="Indicates whether the emissions control equipment controls acid (HCl) gas.",
        ),
        sa.Column(
            "emission_control_equipment_cost",
            sa.Float(),
            nullable=True,
            comment="The total cost to install a piece of emission control equipment.",
        ),
        sa.Column(
            "emission_control_operating_date",
            sa.Date(),
            nullable=True,
            comment="The date a piece of emissions control equipment began operating. Derived from month and year columns in the raw data.",
        ),
        sa.Column(
            "emission_control_retirement_date",
            sa.Date(),
            nullable=True,
            comment="The expected or actual retirement date for a piece of emissions control equipment. Derived from month and year columns in the raw data.",
        ),
        sa.ForeignKeyConstraint(
            ["data_maturity"],
            ["data_maturities.code"],
        ),
        sa.ForeignKeyConstraint(
            ["operational_status_code"],
            ["operational_status_eia.code"],
        ),
        sa.ForeignKeyConstraint(
            ["plant_id_eia"],
            ["plants_entity_eia.plant_id_eia"],
        ),
        sa.PrimaryKeyConstraint(
            "report_year", "plant_id_eia", "emission_control_id_pudl"
        ),
    )
    op.create_table(
        "boiler_emissions_control_equipment_assn_eia860",
        sa.Column("report_date", sa.Date(), nullable=False, comment="Date reported."),
        sa.Column(
            "plant_id_eia",
            sa.Integer(),
            nullable=False,
            comment="The unique six-digit facility identification number, also called an ORISPL, assigned by the Energy Information Administration.",
        ),
        sa.Column(
            "boiler_id", sa.Text(), nullable=False, comment="Alphanumeric boiler ID."
        ),
        sa.Column(
            "emission_control_id_type",
            sa.Text(),
            nullable=False,
            comment="The type of emissions control id: so2, nox, particulate, or mercury.",
        ),
        sa.Column(
            "emission_control_id_eia",
            sa.Text(),
            nullable=False,
            comment="The emission control ID used to collect so2, nox, particulate, and mercury emissions data. This column shoudl be used in conjunction with emissions_control_type as it's not guaranteed to be unique.",
        ),
        sa.Column(
            "data_maturity",
            sa.Text(),
            nullable=True,
            comment="Level of maturity of the data record. Some data sources report less-than-final data. PUDL sometimes includes this data, but use at your own risk.",
        ),
        sa.ForeignKeyConstraint(
            ["data_maturity"],
            ["data_maturities.code"],
        ),
        sa.ForeignKeyConstraint(
            ["plant_id_eia", "boiler_id", "report_date"],
            [
                "boilers_eia860.plant_id_eia",
                "boilers_eia860.boiler_id",
                "boilers_eia860.report_date",
            ],
        ),
        sa.PrimaryKeyConstraint(
            "report_date",
            "plant_id_eia",
            "boiler_id",
            "emission_control_id_type",
            "emission_control_id_eia",
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("boiler_emissions_control_equipment_assn_eia860")
    op.drop_table("emissions_control_equipment_eia860")
    op.drop_table("denorm_emissions_control_equipment_eia860")
    # ### end Alembic commands ###
