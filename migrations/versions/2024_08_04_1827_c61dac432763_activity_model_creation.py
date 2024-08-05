"""Activity model creation

Revision ID: c61dac432763
Revises: 180415d3eca3
Create Date: 2024-08-04 18:27:26.476862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c61dac432763"
down_revision: Union[str, None] = "180415d3eca3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "activitys",
        sa.Column("mensuration", sa.Float(), nullable=False),
        sa.Column(
            "done_date",
            sa.DateTime(),
            server_default="2024-08-04 15:27:26.104880",
            nullable=False,
        ),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.CheckConstraint(
            "mensuration > 0", name=op.f("ck_activitys_mensuration_gt_zero")
        ),
        sa.ForeignKeyConstraint(
            ["task_id"], ["tasks.id"], name=op.f("fk_activitys_task_id_tasks")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_activitys")),
    )
    op.create_index(op.f("ix_activitys_id"), "activitys", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_activitys_id"), table_name="activitys")
    op.drop_table("activitys")
    # ### end Alembic commands ###